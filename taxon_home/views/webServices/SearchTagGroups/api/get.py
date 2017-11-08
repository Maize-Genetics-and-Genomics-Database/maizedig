import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import TagGroup, Picture
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceArray, LimitDict


class GetAPI:
    
    def __init__(self, limit=10, offset=0, user=None, fields=None, unlimited=False):
        self.limit = limit
        self.offset = offset
        self.unlimited = unlimited
        self.user = user
        self.fields = fields

    '''
        Gets the tag groups for the given image
        
        @param imageKey: The primary key for the image or the image
        @param isKey: Whether the first argument is a key object or not (default: true)
    '''
    def getTagGroupsByImageID(self, imageKey, isKey=True):
        metadata = WebServiceArray()

        try:
            if (isKey):
                image = Picture.objects.get(pk__exact=imageKey)
            else:
                image = imageKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_IMAGE_KEY

        if not image.readPermissions(self.user):
            raise Errors.AUTHENTICATION

        if self.unlimited:
            groups = TagGroup.objects.filter(picture__exact=image)[self.offset:]
        else:
            groups = TagGroup.objects.filter(picture__exact=image)[self.offset : self.offset+self.limit]

        for group in groups:
            if group.readPermissions(self.user):
                metadata.put(
                    LimitDict(self.fields, {
                        'id' : group.pk,
                        'user' : group.user.username,
                        'name' : group.name,
                        'dateCreated' : group.dateCreated.strftime("%Y-%m-%d %H:%M:%S"),
                        'lastModified' : group.lastModified.strftime("%Y-%m-%d %H:%M:%S"),
                        'imageId' : group.picture.pk,
                        'isPrivate' : group.isPrivate
                    })
                )

        return metadata

    '''
        Gets the all tag groups for the given image name - Default
        
        @param imageKey: The primary key for the image or the image
        @param isKey: Whether the first argument is a key object or not (default: true)
    '''
    def getTagGroupsByImage(self, imageKey, isKey=True):
        metadata = WebServiceArray()
        
        try:
            if (isKey):
                image = Picture.objects.get(pk__exact=imageKey)
            else:
                image = imageKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_IMAGE_KEY
                
        if not image.readPermissions(self.user):
            raise Errors.AUTHENTICATION

        # get all duplicate image instances with ImageName
        images = Picture.objects.filter(imageName__exact=image.imageName)

        for imageID in images:
            if self.unlimited:
                groups = TagGroup.objects.filter(picture__exact=imageID)[self.offset:]
            else:
                groups = TagGroup.objects.filter(picture__exact=imageID)[self.offset : self.offset+self.limit]

            for group in groups:
                if group.readPermissions(self.user):
                    metadata.put(
                        LimitDict(self.fields, {
                            'id' : group.pk,
                            'user' : group.user.username,
                            'name' : group.name,
                            'dateCreated' : group.dateCreated.strftime("%Y-%m-%d %H:%M:%S"),
                            'lastModified' : group.lastModified.strftime("%Y-%m-%d %H:%M:%S"),
                            'imageId' : group.picture.pk,
                            'isPrivate' : group.isPrivate
                        })
                    )
    
        return metadata
    
    
    '''
        Gets all the tag groups
    '''
    def getTagGroups(self):
        metadata = WebServiceArray()
 
        if self.user and self.user.is_authenticated():
            images = Picture.objects.filter(isPrivate=False) | Picture.objects.filter(user__exact=self.user, isPrivate=True) 
        else:
            images = Picture.objects.filter(isPrivate=False)

        if self.unlimited:
            groups = TagGroup.objects.filter(picture__in=images)[self.offset:]
        else:
            groups = TagGroup.objects.filter(picture__in=images)[self.offset : self.offset+self.limit]
        
        for group in groups:
            if group.readPermissions(self.user):
                metadata.put(
                    LimitDict(self.fields, {
                        'id' : group.pk,
                        'user' : group.user.username,
                        'name' : group.name,
                        'dateCreated' : group.dateCreated.strftime("%Y-%m-%d %H:%M:%S"),
                        'lastModified' : group.lastModified.strftime("%Y-%m-%d %H:%M:%S"),
                        'imageId' : group.picture.pk,
                        'isPrivate' : group.isPrivate
                    })
                )
        
        return metadata
