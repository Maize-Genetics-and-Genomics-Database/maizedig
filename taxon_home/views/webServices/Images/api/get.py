import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import Picture, PictureDefinitionTag, RecentlyViewedPicture
from taxon_home.models import PictureMgdb, PictureGeneID
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject
from taxon_home.views.webServices.Notes.api.get import GetAPI as NotesAPI

class GetAPI:
    def __init__(self, user=None, fields=None):
        self.user = user
        self.fields = fields

    '''
        Gets the metadata associated with an image given the image key
        
        @param imageKey: The primary key for the image or the image
        @param isKey: Whether the first argument is a key object or not (default: true)
        
        @return: A dictionary containing organisms associated with the image and all 
        of the images attributes. The dictionary will also contain error information
        stored in the errorMessage and error fields
    '''
    def getImageMetadata(self, imageKey, isKey=True):
        # TODO: getImageMetadata() should be refactorized because it is used for all image loading parts
        #  including image list even thumbnail image. It potentially has unnecessary database queries.

        organisms = []
        geneIDs = []
        metadata = WebServiceObject()
        
        try:
            if (isKey):
                image = Picture.objects.get(pk__exact=imageKey) 
            else:
                image = imageKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_IMAGE_KEY

        # Get gene information
        geneSymbol = None
        geneName = None
        if image is not None:
            # Gene ID
            pictureGIDs = PictureGeneID.objects.filter(picture__exact=image)
            for picGID in pictureGIDs:
                geneIDs.append({
                    'geneID' : picGID.gene_id,
                    'version' : picGID.version
                })

            pictureMbs = PictureMgdb.objects.filter(picture__exact=image)
            for pMb in pictureMbs:
                geneSymbol = pMb.locus_name
                geneName = pMb.locus_full_name
                break

        if not image.readPermissions(self.user):
            raise Errors.AUTHENTICATION
        
        if not self.fields or 'organisms' in self.fields:
            defTags = PictureDefinitionTag.objects.filter(picture__exact=image)
            
            for tag in defTags:
                organisms.append({
                    'commonName' : tag.organism.common_name,
                    'abbreviation' : tag.organism.abbreviation,
                    'genus' : tag.organism.genus,
                    'species' : tag.organism.species,
                    'id' : tag.organism.pk
                })

        # Get Image Notes Information
        pictureNotesAPI = NotesAPI(self.user)
        pictureNotes = pictureNotesAPI.getNote(imageKey).getObject()
        if pictureNotes:
            notes = pictureNotes['notes']
            notesBy = pictureNotes['user']
        else:
            notes = ''
            notesBy = ''

        metadata.limitFields(self.fields)

        # put in the information we care about
        metadata.put('organisms', organisms)
        metadata.put('description', image.description)
        metadata.put('altText', image.altText)
        metadata.put('uploadedBy', image.user.username)
        metadata.put('uploadDate', image.uploadDate.strftime("%Y-%m-%d %H:%M:%S"))
        metadata.put('url', image.imageName.url)
        metadata.put('thumbnail', image.thumbnail.url)
        metadata.put('id', image.pk)
        metadata.put('geneIDs', geneIDs)
        metadata.put('geneSymbol', geneSymbol)
        metadata.put('geneName', geneName)
        metadata.put('notes', notes)
        metadata.put('notesBy', notesBy)

        # add to recently viewed images if there is a user
        #if self.user and self.user.is_authenticated():
        #    RecentlyViewedPicture.objects.get_or_create(user=self.user, picture=image)[0].save()

        return metadata
