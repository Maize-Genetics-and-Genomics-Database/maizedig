'''
	GetAPI for handling QTL data

    Author: Kyoung Tak Cho
	Creaded Date: December 21, 2018
	Last updated: January 10, 2019
7
'''

import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import PictureQtl
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject

class GetAPI:

    def __init__(self, user=None, fields=None):
        self.user = user
        self.fields = fields

    '''
        Gets all the tags in the database that are private
    '''
    def getQtl(self, imageKey):
        metadata = WebServiceObject()

        try:
            pictureQtl = PictureQtl.objects.filter(picture__exact=imageKey).order_by('-dateCreated')[:1].get()
        except (ObjectDoesNotExist, ValueError):
            return metadata

        metadata.limitFields(self.fields)

        metadata.put('pq_id', pictureQtl.pk)
        metadata.put('picture', pictureQtl.picture.pk)
        metadata.put('qtl', pictureQtl.qtl)
        metadata.put('user', pictureQtl.user.username)
        metadata.put('dateCreated', pictureQtl.dateCreated.strftime("%Y-%m-%d %H:%M:%S"))

        return metadata
