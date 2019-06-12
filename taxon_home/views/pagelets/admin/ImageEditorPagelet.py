'''
    Pagelet for the Image Editor which is both an admin
    and a public application

    Author: Andrew Oberlin
    Date: August 5, 2012

    Modified by Kyoung Tak Cho
    Date: November 1, 2016
    Last Updated: Nov 14 14:46:18 CDT 2017
'''

from renderEngine.PageletBase import PageletBase
import simplejson as json
from taxon_home.views.webServices.SearchGeneLinks.api.get import GetAPI as GeneLinkAPI
from taxon_home.views.webServices.SearchTags.api.get import GetAPI as TagAPI
from taxon_home.views.webServices.SearchTagGroups.api.get import GetAPI as TagGroupAPI
from taxon_home.views.webServices.Images.api.get import GetAPI as ImageMetadataAPI
from taxon_home.models import Picture, RecentlyViewedPicture
from django.core.exceptions import ObjectDoesNotExist

class ImageEditorPagelet(PageletBase):
    '''
        Renders the center of the home page        
    
        Params: request -- the Django request object with the POST & GET args
        
        Returns: Dictionary of arguments for rendering this pagelet
    '''
    def doProcessRender(self, request):
        self.setLayout('admin/imageEditor.html')
        try:
            imageKey = request.GET.get('imageId', None)
            if (imageKey):
                image = Picture.objects.get(pk__exact=imageKey)
                
                # initialize tagging APIs
                tagGroupAPI = TagGroupAPI(unlimited=True)
                tagAPI = TagAPI(unlimited=True)
                geneLinkAPI = GeneLinkAPI(unlimited=True)
                tagGroups = tagGroupAPI.getTagGroupsByImage(image, False).getObject()
                
                for group in tagGroups:
                    
                    tags = tagAPI.getTagsByTagGroup(group['id']).getObject()
                    #tags = tagAPI.getTagsByImage(group['imageId']).getObject()
                    #print('tags= ' + json.dumps(tags))
                    #print('group id= ' + json.dumps(group))
                    for tag in tags:
                        geneLinks = geneLinkAPI.getGeneLinksByTag(tag['id']).getObject()
                        tag['geneLinks'] = geneLinks
                        #print('tag= ' + json.dumps(tag))
                    group['tags'] = tags
                    
                    
                #print('tagGroups= ' + json.dumps(tagGroups))
                    
                # initialize image metadata API
                imageMetadataAPI = ImageMetadataAPI(request.user)
                imageMetadata = imageMetadataAPI.getImageMetadata(image, isKey=False).getObject()

                # add to recently viewed images - modified by ktcho, 2017.10.09
                # moved from get.py to here (add only when user view image via image editor/viewer)
                if (request.user):
                    RecentlyViewedPicture.objects.get_or_create(user=request.user, picture=image)[0].save()

                return {
                    'imageMetadata' : json.dumps(imageMetadata),
                    'tagGroups' : json.dumps(tagGroups),
                    'image' : image
                }
            else:
                self.setLayout('public/404Media.html')
                return {}
        except ObjectDoesNotExist:
            self.setLayout('public/404Media.html')
            return {}
        except KeyError:
            self.setLayout('public/404Media.html')
            return {}
