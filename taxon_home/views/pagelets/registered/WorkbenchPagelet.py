'''
    Pagelet for the user Workbench
    
    Author: Andrew Oberlin
    Date: July 23, 2012
'''
from renderEngine.PageletBase import PageletBase
from taxon_home.models import Picture, RecentlyViewedPicture, Tag, TagGroup, GeneLink

class WorkbenchPagelet(PageletBase):
    '''
        Renders the user workbench for the website        
    
        Params: request -- the Django request object with the POST & GET args
        
        Returns: Dictionary of arguments for rendering this pagelet
    '''
    def doProcessRender(self, request):
        self.setLayout('registered/workbench.html')

        # check imageID request for default showing image (image showing from other page like iSearch result page)
        dlImageID = request.GET.get('dliid', None)
        if(dlImageID):
            # add to recently viewed images - modified by ktcho, 2017.10.09
            # moved from get.py to here (add only when user view image via image editor/viewer)
            if (request.user):
                image = Picture.objects.filter(pk__exact=dlImageID)
                RecentlyViewedPicture.objects.get_or_create(user=request.user, picture=image[0])[0].save()

        userImages = Picture.objects.filter(user__exact=request.user)

        myImages = []
                
        #
        for image in userImages:
            permissions = 'public'
            if image.isPrivate:
                permissions = 'private'
            myImages.append({
                'permissions' : permissions,
                'image' : image
            })
            
        recentImages = RecentlyViewedPicture.objects.filter(user__exact=request.user).order_by('-lastDateViewed')[:10]
        
        userTags = Tag.objects.filter(user__exact=request.user).order_by('dateCreated')
        myTags = []
                
        #
        for tag in userTags:
            permissions = 'public'
            if tag.isPrivate:
                permissions = 'private'
            myTags.append({
                'permissions' : permissions,
                'tag' : tag
            })


        userTagGroups = TagGroup.objects.filter(user__exact=request.user).order_by('dateCreated')
        myTagGroups = []
                
        #
        for tagGroup in userTagGroups:
            permissions = 'public'
            if tagGroup.isPrivate:
                permissions = 'private'
            myTagGroups.append({
                'permissions' : permissions,
                'tagGroup' : tagGroup
            })
            
        userGeneLinks = GeneLink.objects.filter(user__exact=request.user).order_by('dateCreated')
        myGeneLinks = []
                
        #
        for geneLink in userGeneLinks:
            permissions = 'public'
            if geneLink.isPrivate:
                permissions = 'private'
            myGeneLinks.append({
                'permissions' : permissions,
                'geneLink' : geneLink
            })



        return {
            'myImages' : myImages,
            'recentImages' : recentImages,
            'myTags' : myTags,
            'myTagGroups' : myTagGroups,
            'myGeneLinks' : myGeneLinks,
            'dlImageID' : dlImageID
        }
