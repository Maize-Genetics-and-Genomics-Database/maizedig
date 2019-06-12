'''
	PostAPI for handling QTL data

	Author: Kyoung Tak Cho
	Creaded Date: December 21, 2018
	Last updated: January 10, 2019
'''

import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import Picture, PictureQtl
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject
from django.db import transaction, DatabaseError

class PostAPI:

    def __init__(self, user, fields=None):
        self.user = user
        self.fields = fields

    '''
        Creates a new note with the given parameters
        
        @param qtl
        @param pq_id
        @param PictureID
    '''
    @transaction.commit_on_success
    def addQtl(self, qtl, pq_id, imageKey):
        metadata = WebServiceObject()

        print 'test 1'

        # get picture instance with imageKey
        try:
            image = Picture.objects.get(pk__exact=imageKey)
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_IMAGE_KEY

        if not self.user:
            raise Errors.NO_USER_KEY
        else:
            userID = self.user

        try:
            # save the new note
            if pq_id:
                # update
                pictureQtl = PictureQtl.objects.get(pk__exact=pq_id)
                if pictureQtl:
                    pictureQtl.qtl = qtl
                    pictureQtl.picture = image
                    pictureQtl.user = userID
                    pictureQtl.save()
                else:
                    # error
                    print 'Error: no PictureQtl.pk found!'
            else:
                # add new
                pictureQtl = PictureQtl(qtl=qtl, picture=image, user=userID)
                print 'test: trying store qtl.'
                pictureQtl.save()
                print 'test: qtl saved.'

        except DatabaseError as e:
            transaction.rollback()
            raise Errors.INTEGRITY_ERROR.setCustom(str(e))

        # limit metadata return
        metadata.limitFields(self.fields)

        # add new tag to response for success
        metadata.put('pq_id', pictureQtl.pk)
        metadata.put('picture', pictureQtl.picture.pk)
        metadata.put('qtl', pictureQtl.qtl)
        metadata.put('user', pictureQtl.user.username)
        metadata.put('dateCreated', pictureQtl.dateCreated.strftime("%Y-%m-%d %H:%M:%S"))

        return metadata
