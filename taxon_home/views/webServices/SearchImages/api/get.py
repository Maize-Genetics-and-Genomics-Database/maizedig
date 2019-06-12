"""
    GetAPI for SearchImages
    @methods
      getImageMetadataByOrganism()
      getImageMetadata()
      getImageMetadataForiSearch()
    @fields
      fields
      limit
      offset
      unlimited
      user

    Updated by Kyoung Tak Cho
    Last Updated: Jan 14 20:30:56 CDT 2018
"""
from taxon_home.models import Picture, PictureDefinitionTag
from taxon_home.models import PictureNotes, PictureMgdb, PictureGeneID
from renderEngine.WebServiceObject import WebServiceArray, WebServiceObject, LimitDict
from taxon_home.views.webServices.Images.api.get import GetAPI as ImageMetadataAPI

class GetAPI:
    def __init__(self, limit=10, offset=0, user=None, fields=None, unlimited=False):
        self.user = user
        self.fields = fields
        self.limit = limit
        self.offset = offset
        self.unlimited = unlimited

    '''
        Gets theimage  metadata associated with a set of organisms 
        
        @param organismId: A list of organism ids
        
        @return: A dictionary containing organisms associated with the image and all 
        of the images attributes. The dictionary will also contain error information
        stored in the errorMessage and error fields
    '''
    def getImageMetadataByOrganism(self, organismId):
        metadata = WebServiceObject()
        
        if self.user and self.user.is_authenticated():
            allowedImages = Picture.objects.filter(isPrivate=False) | Picture.objects.filter(user__exact=self.user, isPrivate=True) 
        else:
            allowedImages = Picture.objects.filter(isPrivate=False)
        
        defTags = []    
        
        if self.unlimited:
            for orgId in organismId:
                defTags.append(PictureDefinitionTag.objects.filter(organism__exact=orgId, picture__in=allowedImages)[self.offset:])
        else:
            for orgId in organismId:
                defTags.append(PictureDefinitionTag.objects.filter(organism__exact=orgId, picture__in=allowedImages)[self.offset:self.offset + self.limit])   

        closedSet = {}
        imageMetadata = {}
        imageFields = set(['id' , 'url', 'uploadDate', 'description', 'uploadedBy'])
        if self.fields:
            newImageFields = imageFields.intersection(set(self.fields))
            if newImageFields:
                imageFields = newImageFields
        imageMetadataAPI = ImageMetadataAPI(self.user, imageFields)
        
        for orgTags in defTags:
            for tag in orgTags:
                if not closedSet.has_key(tag.picture.pk):
                    closedSet[tag.picture.pk] = imageMetadataAPI.getImageMetadata(tag.picture, False).getObject()
                if imageMetadata.has_key(tag.organism.pk):
                    imageMetadata[tag.organism.pk]['images'].append(closedSet[tag.picture.pk])
                else:
                    imageMetadata[tag.organism.pk] = {
                        'images' : [closedSet[tag.picture.pk]],
                        'organism' : {
                            'id' : tag.organism.pk,
                            'commonName' : tag.organism.common_name,
                            'abbreviation' : tag.organism.abbreviation,
                            'genus' : tag.organism.genus,
                            'species' : tag.organism.species
                        }
                    }
                    
        if len(imageMetadata) != len(organismId):
            for orgId in organismId:
                if not imageMetadata.has_key(orgId):
                    imageMetadata[orgId] = []
        
        metadata.setObject(LimitDict(self.fields, imageMetadata))
        
        return metadata
    
    '''
        Gets the metadata associated with an image given the image key
        
        @param organismId: A list of organism ids
        
        @return: A dictionary containing organisms associated with the image and all 
        of the images attributes. The dictionary will also contain error information
        stored in the errorMessage and error fields
    '''
    def getImageMetadata(self):
        metadata = WebServiceArray()
        
        if self.user and self.user.is_authenticated():
            if self.unlimited:
                allowedImages = (Picture.objects.filter(isPrivate=False) | Picture.objects.filter(user__exact=self.user, isPrivate=True))[self.offset:]
            else:
                allowedImages = (Picture.objects.filter(isPrivate=False) | Picture.objects.filter(user__exact=self.user, isPrivate=True))[self.offset:self.offset+self.limit]
        else:
            if self.unlimited:
                allowedImages = Picture.objects.filter(isPrivate=False)[self.offset:]
            else:
                allowedImages = Picture.objects.filter(isPrivate=False)[self.offset:self.offset+self.limit]

        imageMetadataAPI = ImageMetadataAPI(self.user, self.fields)
        
        for image in allowedImages:
            metadata.put(imageMetadataAPI.getImageMetadata(image, False).getObject())

        return metadata

    '''
        Gets the metadata associated with an image given the image key

        Created by Kyoung Tak Cho, 12.03.2016
    '''
    def getImageMetadataForiSearch(self, query):
        metadata = WebServiceArray()
        imageMetadata = {}

        # Image description
        iDescImages = Picture.objects.filter(description__icontains=query[0])[self.offset:self.offset+self.limit]

        # Image notes
        iNoteImages = []
        picturesIN = []
        iNotes = PictureNotes.objects.filter(notes__icontains=query[0])
        for note in iNotes:
            pictureID = note.picture.pk
            if pictureID not in picturesIN:
                iNoteImages.extend(Picture.objects.filter(id__exact=pictureID))
                picturesIN.append(pictureID)
        iNoteImages = iNoteImages[self.offset:self.offset+self.limit]

        # Gene name
        gNameImages = []
        picturesGN = []
        pMgdbs = PictureMgdb.objects.filter(locus_full_name__icontains=query[0])
        for pMgdb in pMgdbs:
            pictureID = pMgdb.picture.pk
            if pictureID not in picturesGN:
                gNameImages.extend(Picture.objects.filter(id__exact=pictureID))
                picturesGN.append(pictureID)
        gNameImages = gNameImages[self.offset:self.offset+self.limit]

        # Gene Symbol
        gSymbolImages = []
        picturesGS = []
        pMgdbs = PictureMgdb.objects.filter(locus_name__icontains=query[0])
        for pMgdb in pMgdbs:
            pictureID = pMgdb.picture.pk
            if pictureID not in picturesGS:
                gSymbolImages.extend(Picture.objects.filter(id__exact=pictureID))
                picturesGS.append(pictureID)
        gSymbolImages = gSymbolImages[self.offset:self.offset+self.limit]

        # Gene ID
        gIDImages = []
        pictureGIs = []
        pIDs = PictureGeneID.objects.filter(gene_id__icontains=query[0])
        for pID in pIDs:
            pictureID = pID.picture.pk
            if pictureID not in pictureGIs:
                gIDImages.extend(Picture.objects.filter(id__exact=pictureID))
                pictureGIs.append(pictureID)
        gIDImages = gIDImages[self.offset:self.offset+self.limit]

        imageMetadataAPI = ImageMetadataAPI(self.user, self.fields)

        for image in iDescImages:
            if imageMetadata.has_key(0):
                imageMetadata[0]['images'].append(imageMetadataAPI.getImageMetadata(image, False).getObject())
            else:
                imageMetadata[0] = {'images' : [imageMetadataAPI.getImageMetadata(image, False).getObject()]}
        for image in iNoteImages:
            if imageMetadata.has_key(1):
                imageMetadata[1]['images'].append(imageMetadataAPI.getImageMetadata(image, False).getObject())
            else:
                imageMetadata[1] = {'images' : [imageMetadataAPI.getImageMetadata(image, False).getObject()]}
        for image in gNameImages:
            if imageMetadata.has_key(2):
                imageMetadata[2]['images'].append(imageMetadataAPI.getImageMetadata(image, False).getObject())
            else:
                imageMetadata[2] = {'images' : [imageMetadataAPI.getImageMetadata(image, False).getObject()]}
        for image in gSymbolImages:
            if imageMetadata.has_key(3):
                imageMetadata[3]['images'].append(imageMetadataAPI.getImageMetadata(image, False).getObject())
            else:
                imageMetadata[3] = {'images' : [imageMetadataAPI.getImageMetadata(image, False).getObject()]}
        for image in gIDImages:
            if imageMetadata.has_key(4):
                imageMetadata[4]['images'].append(imageMetadataAPI.getImageMetadata(image, False).getObject())
            else:
                imageMetadata[4] = {'images' : [imageMetadataAPI.getImageMetadata(image, False).getObject()]}

        metadata.setObject(LimitDict(self.fields, imageMetadata))

        return metadata

