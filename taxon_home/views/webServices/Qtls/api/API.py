'''
    QTL webServices API

    Author: Kyoung Tak Cho
	Creaded Date: December 21, 2018
	Last updated: January 10, 2019
'''

import taxon_home.views.util.ErrorConstants as Errors
import taxon_home.views.util.Util as Util
from get import GetAPI
from post import PostAPI

'''
    Gets the recent note information given imageID and userID
    @param request: Django Request object to be used to parse the query
'''
def getQtl(request):
    imageKey = request.GET.get('pictureID', None)

    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.GET, 'fields')
    getAPI = GetAPI(request.user, fields)

    return getAPI.getQtl(imageKey)

'''
    Adds a new and returns the representation of the newly created gene link.dd
    @param request: Django Request object to be used to parse the query
'''
def addQtl(request):
    # get new note information
    qtl = request.POST.get('qtl', None)
    pq_id = request.POST.get('pq_id', None)
    imageKey = request.POST.get('pictureID', None)

    print 'test addQql()'

    if not imageKey:
        raise Errors.NO_IMAGE_KEY

    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.POST, 'fields')

    postAPI = PostAPI(request.user, fields)
    return postAPI.addQtl(qtl, pq_id, imageKey)

