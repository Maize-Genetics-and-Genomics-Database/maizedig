from renderEngine.WebServiceObject import WebServiceObject
import taxon_home.views.util.ErrorConstants as Errors
import taxon_home.views.util.Util as Util
from get import GetAPI
from put import PutAPI
from post import PostAPI
from delete import DeleteAPI

def getImageMetadata(request):
    renderObj = WebServiceObject()
    if request.GET.has_key('id'):
        # the key for lookup and the image it is attached to
        imageKey = request.GET['id']
        fields = Util.getDelimitedList(request.GET, 'fields')
        getAPI = GetAPI(request.user, fields)
        try:
            renderObj = getAPI.getImageMetadata(imageKey)
        except Errors.WebServiceException as e:
            renderObj.setError(e)
    else:
        renderObj.setError(Errors.NO_IMAGE_KEY)
    
    return renderObj

def createImageMetadata(request):
    renderObj = WebServiceObject()
    
    # these should overwrite current metadata
    image = request.FILES.get('image', None)
    description = request.POST.get('description', None)
    altText = request.POST.get('altText', None)
    organisms = Util.getDelimitedList(request.POST, 'organisms')
    fields = Util.getDelimitedList(request.POST, 'fields')
    
    if image:
        postAPI = PostAPI(request.user, fields)
        renderObj = postAPI.createImageMetadata(image, description, altText, organisms)
    else:
        raise Errors.MISSING_PARAMETER.setCustom('image')
    
    return renderObj

def editImageMetadata(request):
    renderObj = WebServiceObject()
    
    # required parameters
    imageKey = request.PUT.get('id', None)
    if not imageKey:
        raise Errors.NO_IMAGE_KEY
    
    # these should overwrite current metadata
    description = request.PUT.get('description', None)
    altText = request.POST.get('altText', None)
    organisms = Util.getDelimitedList(request.PUT, 'organisms')
    fields = Util.getDelimitedList(request.PUT, 'fields')
    
    if description or organisms:
        putAPI = PutAPI(request.user, fields)
        renderObj = putAPI.editImageMetadata(imageKey, description, altText, organisms)
    else:
        raise Errors.NOT_MODIFIED
    
    return renderObj

def deleteImage(request):
    # required parameters
    imageKey = request.DELETE.get('id', None)
    if not imageKey:
        raise Errors.NO_IMAGE_KEY
    
    fields = Util.getDelimitedList(request.GET, 'fields')
    
    deleteAPI = DeleteAPI(request.user, fields)
    return deleteAPI.deleteImage(imageKey)


