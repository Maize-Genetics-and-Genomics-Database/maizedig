'''
    Pagelet for the Search Page
    
    Author: Andrew Oberlin
    Date: August 21, 2012

    Modified by Kyoung Tak Cho
    Date: November 15, 2016
    Last Updated: May 9 14:06:25 CDT 2018
'''
from renderEngine.PageletBase import PageletBase
#from taxon_home.models import PictureDefinitionTag
from taxon_home.models import Picture

class iSearchPagelet(PageletBase):
    '''
        Used to set the extra parameters for executing the search simply
        
        @param: searchParams -- parameters for searching the image database
        
        @return: self object to allow for easy chaining
    '''
    def setSearchParams(self, searchParams):
        self.searchParams = searchParams
        return self
        
    '''
        Renders the navigation bar for the website        
    
        Params: request -- the Django request object with the POST & GET args
        
        Returns: Dictionary of arguments for rendering this pagelet
    '''
    def doProcessRender(self, request):
        self.setLayout('public/iSearch.html')
        
        limit = 8
        
        candidateInfo = list()
        candidates = self.searchParams['candidates']
        
        for category in candidates:
            if len(category[0]) > 1:
                numImages = len(category) - 1
                pages = numImages/limit + 1
                candidateInfo.append(('par 1', category[0], str(candidates.index(category)), pages, numImages))

        return {
            'candidateInfo': candidateInfo,
            'limit': limit,
            'imagesPerRow' : 4,
            'user' : request.user,
            'query' : self.searchParams['query']
        }
