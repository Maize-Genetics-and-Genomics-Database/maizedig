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
from taxon_home.views.pagelets.public.iSearchPagelet import iSearchPagelet
from taxon_home.views.pagelets.public.GBrowseSearchPagelet import GBrowseSearchPagelet
from taxon_home.views.pagelets.public.NavBarPagelet import NavBarPagelet
from taxon_home.views.pagelets.public.FooterPagelet import FooterPagelet
from taxon_home.models import Picture, GeneLink, Tag, Feature
#from taxon_home.models import Organism
#from taxon_home.models import GeneLink
#from taxon_home.models import Feature
#from django.db.models import Q
from taxon_home.views.util import Util

class Application(ApplicationBase):
    def doProcessRender(self, request):
        self.addPageletBinding('navBar', NavBarPagelet())

        numSearch = 0
        searchCats = 0
        searchImageDesc = str(request.GET.get('searchImageDesc', '')).lower() == "true"
        searchImageNotes = str(request.GET.get('searchImageNotes', '')).lower() == "true"
        searchGeneName = str(request.GET.get('searchGeneName', '')).lower() == "true"
        searchGeneSymbol = str(request.GET.get('searchGeneSymbol', '')).lower() == "true"
        searchGeneID = str(request.GET.get('searchGeneID', '')).lower() == "true"
        query = Util.getDelimitedList(request.GET,'query')
        if not query:
            query = ''

        candidates = [['Image Description'], ['Image Notes'], ['Gene Name'], ['Gene Symbol'], ['Gene ID']]

        if searchImageDesc:
            pictures = Picture.objects.filter(description__icontains=query[0])
            for picture in pictures:
                candidates[0].append(picture)
        if searchImageNotes:
            #featureID = feature.objects.filter()
            #geneLink = GeneLink.objects.get(feature_id__exact=featureID)
            #pictureID = geneLink.
            #pictures = Picture.objects.filter(notes__icontains=query[0])
            pictures = Picture.objects.filter(imageName__icontains=query[0])
            for picture in pictures:
                candidates[1].append(picture)
        if searchGeneName:
            #pictures = Picture.objects.filter(description__icontains=query[0])
            #for picture in pictures:
            #    candidates[2].append(picture)

            tags = Tag.objects.filter(name__icontains=query[0])
            gNameImages = []
            pictureIDs = []
            for tag in tags:
                pictureID = tag.group.picture.pk
                if not pictureID in pictureIDs:
                    gNameImages.extend(Picture.objects.filter(id__exact=pictureID))
                    pictureIDs.append(pictureID)
                    candidates[2].append(pictureID)

        #if searchGeneID:
        #    #pictures = Picture.objects.filter(description__icontains=query[0])
        #    features = Feature.objects.filter(name__icontains=query[0])
        #    for feature in features:
        #        candidates[4].append(feature)
            '''
            gIDImages = []
            pictureIDs = []
            features = Feature.objects.filter(name__icontains=query[0])[0:10]
            #features = Feature.objects.filter(name__icontains=query[0])
            print len(features)
            for feature in features:
                #pictureID = GeneLink.objects.filter(feature__exact=feature.feature_id).tag.group.picture.pk
                genelink = GeneLink.objects.get(feature_id__exact=feature.feature_id)
                pictureID = genelink.tag.group.picture.pk
                if not pictureID in pictureIDs:
                    #gIDImages.extend(Picture.objects.filter(id__exact=pictureID))
                    pictureIDs.append(pictureID)
                    candidates[4].append(pictureID)
            '''

        formatQuery = ""
        if query:
            formatQuery += 'General Query: "' + ", ".join(query) + '"'


        search = {
            'candidates' : candidates,
            'query' : query[0]
        }

        #if searchImageDesc:
        numSearch += 1
        #self.addPageletBinding('center-' + str(numSearch), ImageSearchPagelet().setSearchParams(search))
        self.addPageletBinding('center-' + str(numSearch), iSearchPagelet().setSearchParams(search))

        args = {
            'title' : 'iSearch',
            'numPagelets' : numSearch
        }
        self.setApplicationLayout('public/iSearch.html', args)

        self.addPageletBinding('footer', FooterPagelet())

'''
    Used for mapping to the url in urls.py
'''
def renderAction(request):
    return Application().render(request)

