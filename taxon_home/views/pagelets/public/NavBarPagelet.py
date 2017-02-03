'''
	Pagelet for the Nav Bar on many pages
	
	Author: Andrew Oberlin
	Date: July 23, 2012
'''
from renderEngine.PageletBase import PageletBase

class NavBarPagelet(PageletBase):
	#def __init__(self, addHelpButton=False):
	def __init__(self, addHelpButton=False, isHomePage=False):
		self.addHelpButton = addHelpButton
		self.isHomePage = isHomePage
	
	'''
		Renders the navigation bar for the website		
	
		Params: request -- the Django request object with the POST & GET args
		
		Returns: Dictionary of arguments for rendering this pagelet
	'''
	def doProcessRender(self, request):
		self.setLayout('public/navBar.html')
		
		is_admin_page = False
		
		if (request.method == "GET" and request.GET.has_key('add_login')):                
			is_admin_page = request.GET['add_login']

		return {
			'is_admin_page' : is_admin_page,
			'addHelpButton' : self.addHelpButton,
			'is_home_page' : self.isHomePage
		}
