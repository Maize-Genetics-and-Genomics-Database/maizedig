import taxon_home.views.util.ErrorConstants as Errors
import taxon_home.views.util.Util as Util
from get import GetAPI
from post import PostAPI
#from put import PutAPI
#from delete import DeleteAPI

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
    imageKey = request.POST.get('pictureID', None)

    if not imageKey:
        raise Errors.NO_IMAGE_KEY

    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.POST, 'fields')

    postAPI = PostAPI(request.user, fields)
    return postAPI.addNote(notes, imageKey)

