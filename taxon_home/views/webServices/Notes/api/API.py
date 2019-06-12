'''
    Image notes webServices API

    Author: Kyoung Tak Cho
	Date: Oct. 23, 2017
    Last Updated: Jan 10 12:16:09 CDT 2019
'''

import taxon_home.views.util.ErrorConstants as Errors
import taxon_home.views.util.Util as Util
from get import GetAPI
from post import PostAPI

'''
    Gets the recent note information given imageID and userID
    @param request: Django Request object to be used to parse the query
'''
def getNote(request):
    imageKey = request.GET.get('pictureID', None)

    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.GET, 'fields')
    getAPI = GetAPI(request.user, fields)

    return getAPI.getNote(imageKey)

'''
    Adds a new and returns the representation of the newly created gene link.dd
    @param request: Django Request object to be used to parse the query
'''
def addNote(request):
    # get new note information
    notes = request.POST.get('notes', None)
    pn_id = request.POST.get('pn_id', None)
    imageKey = request.POST.get('pictureID', None)

    if not imageKey:
        raise Errors.NO_IMAGE_KEY

    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.POST, 'fields')

    postAPI = PostAPI(request.user, fields)
    return postAPI.addNote(notes, pn_id, imageKey)

