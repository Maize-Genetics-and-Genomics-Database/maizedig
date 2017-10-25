import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import Picture, PictureNotes
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject
from django.db import transaction, DatabaseError

class PostAPI:

    def __init__(self, user, fields=None):
        self.user = user
        self.fields = fields

    '''
        Creates a new note with the given parameters
        
        @param notes
        @param PictureID
    '''
    @transaction.commit_on_success
    def addNote(self, notes, imageKey):
        metadata = WebServiceObject()

        # get picture instance with imageKey
        try:
            image = Picture.objects.get(pk__exact=imageKey)
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_IMAGE_KEY

        if not self.user:
            raise Errors.NO_USER_KEY
        else:
            userID = self.user

        # save the new note
        pictureNotes = PictureNotes(notes=notes, picture=image, user=userID)
        try:
            pictureNotes.save()
        except DatabaseError as e:
            transaction.rollback()
            raise Errors.INTEGRITY_ERROR.setCustom(str(e))

        # limit metadata return
        metadata.limitFields(self.fields)

        # add new tag to response for success
        metadata.put('pn_id', pictureNotes.pk)
        metadata.put('picture', pictureNotes.picture.pk)
        metadata.put('notes', pictureNotes.notes)
        metadata.put('user', pictureNotes.user.username)
        metadata.put('dateCreated', pictureNotes.dateCreated.strftime("%Y-%m-%d %H:%M:%S"))

        return metadata
