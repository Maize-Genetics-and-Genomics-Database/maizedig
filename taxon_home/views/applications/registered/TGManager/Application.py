'''
	Application for the Logout Handler of the DOME
	URL: /logout_handler
	
	Author: Kyoung Tak Cho
	Date: July 28, 2016
'''
from renderEngine.RegisteredApplicationBase import RegisteredApplicationBase
from taxon_home.views.pagelets.registered.NavBarPagelet import NavBarPagelet
from taxon_home.views.pagelets.registered.TGManagerPagelet import TGManagerPagelet
from taxon_home.views.pagelets.public.FooterPagelet import FooterPagelet

class Application(RegisteredApplicationBase):
	def doProcessRender(self, request):
		args = {
			'title' : 'Tag/GeneLink Manager'
		}
		
		self.setApplicationLayout('registered/base.html', args)
		self.addPageletBinding('navBar', NavBarPagelet())
		self.addPageletBinding('center-1', TGManagerPagelet())
		self.addPageletBinding('footer', FooterPagelet())

'''
	Used for mapping to the url in urls.py
'''      	
def renderAction(request):
	return Application().render(request)

