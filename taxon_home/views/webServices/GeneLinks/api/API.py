import taxon_home.views.util.ErrorConstants as Errors
import taxon_home.views.util.Util as Util
from get import GetAPI
from post import PostAPI
from delete import DeleteAPI
import logging

'''
    Get an instance of a logger
'''
#logger = logging.getLogger('django')
logger = logging.getLogger(__name__)
#logger = logging.getLogger('BioDIG.debug')
#logger = logging.getLogger('BioDIG')

'''
    Gets the information for a tag given its key
    
    @param request: Django Request object to be used to parse the query
'''
def getGeneLink(request):
    # read in crucial parameters
    geneLinkKey = request.GET.get('id', None)
    
    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.GET, 'fields')
    getAPI = GetAPI(request.user, fields)

    if not geneLinkKey:
        raise Errors.NO_GENE_LINK_KEY

    # logging TEST
    logger.error('[DEBUG] Logging TEST')
    logger.debug('[DEBUG] Logging TEST')
    
    # the key for lookup and the image it is attached to
    return getAPI.getGeneLink(geneLinkKey)

'''
    Creates a new gene link and returns the representation of the newly created gene link.
    
    @param request: Django Request object to be used to parse the query
'''
def createGeneLink(request):
    # get tagId for new gene link
    tagId = request.POST.get('tagId', None)

    if not tagId:
        raise Errors.NO_TAG_KEY
    
    name = request.POST.get('name', None)
    allele = request.POST.get('allele', None)
    organismId = request.POST.get('organismId', None)
    
    # read in optional parameters and initialize the API
    fields = Util.getDelimitedList(request.POST, 'fields')
    
    if not (allele or (name and organismId)):
        if not allele:
            raise Errors.MISSING_PARAMETER.setCustom('allele')
        else:
            raise Errors.INVALID_SYNTAX.setCustom('name and organismId required as a pair')
        
    postAPI = PostAPI(request.user, fields)
    return postAPI.createGeneLink(tagId, name, allele, organismId)

'''
    Deletes a tag and returns the information for the tag that was deleted
'''
def deleteGeneLink(request):
    geneLinkKey = request.DELETE.get('id', None)
    
    if not geneLinkKey:
        raise Errors.MISSING_PARAMETER.setCustom('id')
    
    # get optional parameter
    fields = Util.getDelimitedList(request.DELETE, 'fields')
    
    deleteAPI = DeleteAPI(request.user, fields)
    return deleteAPI.deleteGeneLink(geneLinkKey)
    
    
    
