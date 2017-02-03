'''
    Pagelet for the Tag/GeneLink Manager
    
    Author: Kyoung Tak Cho
    Date: July 28, 2016
'''
from renderEngine.PageletBase import PageletBase

class TGManagerPagelet(PageletBase):
    '''
        Renders the Tag/GeneLink Manager page
    
        Params: request -- the Django request object with the POST & GET args
        
        Returns: Dictionary of arguments for rendering this pagelet
    '''
    def doProcessRender(self, request):
        self.setLayout('registered/tgManager.html')

        return {}
