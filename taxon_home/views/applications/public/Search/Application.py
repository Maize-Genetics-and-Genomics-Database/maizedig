'''
    Application for the Search Page of the DOME
    URL: / or /index.html

    Author: Andrew Oberlin
    Date: August 5, 2012

    Modified by Kyoung Tak Cho
    Date: November 1, 2016
'''
from renderEngine.ApplicationBase import ApplicationBase
from taxon_home.views.pagelets.public.ImageSearchPagelet import ImageSearchPagelet
from taxon_home.views.pagelets.public.GBrowseSearchPagelet import GBrowseSearchPagelet
from taxon_home.views.pagelets.public.NavBarPagelet import NavBarPagelet
from taxon_home.views.pagelets.public.FooterPagelet import FooterPagelet
from taxon_home.models import Organism
from taxon_home.models import Picture
from django.db.models import Q
from taxon_home.views.util import Util

class Application(ApplicationBase):
    def doProcessRender(self, request):
        self.addPageletBinding('navBar', NavBarPagelet())

        numSearch = 0
        searchImageDesc = str(request.GET.get('searchImageDesc', '')).lower() == "true"
        searchImageNotes = str(request.GET.get('searchImageNotes', '')).lower() == "true"
        searchGeneName = str(request.GET.get('searchGeneName', '')).lower() == "true"
        searchGeneSymbol = str(request.GET.get('searchGeneSymbol', '')).lower() == "true"
        searchGeneID = str(request.GET.get('searchGeneID', '')).lower() == "true"
        query = Util.getDelimitedList(request.GET,'query')

        #print searchImageDesc
        #print searchImageNotes
        #print searchGeneName
        #print searchGeneSymbol
        #print searchGeneID

        candidate_cat = []

        if searchImageDesc:
            query = Util.getDelimitedList(request.GET, 'query')
            print query
            print len(query)
            candidates_ImgDesc = []
            candidate_cat.append('Image Description')

            if query:
                pictures = Picture.objects.filter(description__icontains=query[0])
                print pictures
                candidates_ImgDesc.append(pictures)

            formatQuery = ""
            if query:
                formatQuery += 'General Query: "' + ", ".join(query) + '"'


        search = {
            'candidate_cat' : candidate_cat,
            'candidates_ImgDesc' : candidates_ImgDesc,
            'query' : formatQuery
        }

        #if searchImageDesc:
        numSearch += 1
        self.addPageletBinding('center-' + str(numSearch), ImageSearchPagelet().setSearchParams(search))

        args = {
            'title' : 'Search',
            'numPagelets' : numSearch
        }
        self.setApplicationLayout('public/search.html', args)

        self.addPageletBinding('footer', FooterPagelet())

'''
        if searchImages or searchGenomes:
            query = Util.getDelimitedList(request.GET,'query')
            organismId = Util.getDelimitedList(request.GET, 'organismId')
            candidates = []

            print query
            print organismId

            if organismId:
                organisms = Organism.objects.filter(pk__in=organismId)
                candidates.append(organisms)
            if query:
                for subquery in query:
                    splitQuery = subquery.strip().split(' ')

                    if (len(splitQuery) == 1):
                        if organismId:
                            candidate = Organism.objects.filter(species=splitQuery[0]).exclude(organism_id__in=organismId)
                        else:
                            candidate = Organism.objects.filter(species=splitQuery[0])
                        candidates.append(candidate)
                    elif(len(splitQuery) == 2):
                        if organismId:
                            candidate = Organism.objects.filter(Q(species=splitQuery[1]) & Q(genus=splitQuery[0])).exclude(organism_id__in=organismId)
                        else:
                            candidate = Organism.objects.filter(Q(species=splitQuery[1]) & Q(genus=splitQuery[0]))
                        candidates.append(candidate)
                    else:
                        if organismId:
                            candidate = Organism.objects.filter(common_name=subquery).exclude(organism_id__in=organismId)
                        else:
                            candidate = Organism.objects.filter(common_name=subquery)
                        candidates.append(candidate)

            formatQuery = ""
            if query:
                formatQuery += 'General Query: "' + ", ".join(query) + '"'
            if organismId:
                amp = " & " if query else ""
                formatQuery += amp + 'Organism Id Query: "' + ", ".join(organismId) + '"'

            search = {
                'candidates' : candidates,
                'query' : formatQuery
            }

            if searchImages:
                numSearch += 1
                self.addPageletBinding('center-' + str(numSearch), ImageSearchPagelet().setSearchParams(search))

            if searchGenomes:
                numSearch += 1
                self.addPageletBinding('center-' + str(numSearch), GBrowseSearchPagelet().setSearchParams(search))
'''

'''
    Used for mapping to the url in urls.py
'''
def renderAction(request):
    return Application().render(request)

