'''
	Pagelet for the Home Page
	
	Author: Andrew Oberlin
	Date: July 23, 2012
'''
from renderEngine.PageletBase import PageletBase
from taxon_home.models import Organism

class BlastPagelet(PageletBase):
	'''
		Renders the center of the home page		
	
		Params: request -- the Django request object with the POST & GET args
		
		Returns: Dictionary of arguments for rendering this pagelet
	'''
	def doProcessRender(self, request):
		self.setLayout('public/blast.html')

		blast_options = Organism.objects.filter(genus__exact='Mycoplasma')
		
		return {
			'blastOptions' : blast_options
		}
