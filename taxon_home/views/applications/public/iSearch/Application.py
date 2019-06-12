'''
    Application for the Image Search
    URL: / or /index.html

    Author: Andrew Oberlin
    Date: August 5, 2012

    Modified by Kyoung Tak Cho
    Date: November 1, 2016
    Last Updated: June 4, 2019
'''
from renderEngine.ApplicationBase import ApplicationBase
from taxon_home.views.pagelets.public.iSearchPagelet import iSearchPagelet
from taxon_home.views.pagelets.public.NavBarPagelet import NavBarPagelet
from taxon_home.views.pagelets.public.FooterPagelet import FooterPagelet
from taxon_home.models import Picture
from taxon_home.models import PictureNotes, PictureMgdb, PictureGeneID
from taxon_home.models import iSearchHistory
from taxon_home.views.util import Util

class Application(ApplicationBase):
    def doProcessRender(self, request):
        self.addPageletBinding('navBar', NavBarPagelet(addHelpButton=True))

        numSearch = 0
        searchCats = list('00000')
        searchImageDesc = str(request.GET.get('searchImageDesc', '')).lower() == "true"
        searchImageNotes = str(request.GET.get('searchImageNotes', '')).lower() == "true"
        searchGeneName = str(request.GET.get('searchGeneName', '')).lower() == "true"
        searchGeneSymbol = str(request.GET.get('searchGeneSymbol', '')).lower() == "true"
        searchGeneID = str(request.GET.get('searchGeneID', '')).lower() == "true"
        query = Util.getDelimitedList(request.GET,'query')
        if not query:
            query = list()
            query.append('')

        #candidates = [['Image Description'], ['Image Notes'], ['Gene Name'], ['Gene Symbol'], ['Gene ID']]
        candidates = [['0'], ['1'], ['2'], ['3'], ['4']]


        if searchImageDesc:
            candidates[0][0] = 'Image Description'
            searchCats[0] = '1'
            pictures = Picture.objects.filter(description__icontains=query[0])
            for picture in pictures:
                candidates[0].append(picture)

        if searchImageNotes:
            candidates[1][0] = 'Image Notes'
            searchCats[1] = '1'
            pNotes = PictureNotes.objects.filter(notes__icontains=query[0])
            pictureIDs = []
            for note in pNotes:
                pictureID = note.picture.pk
                if not pictureID in pictureIDs:
                    pictureIDs.append(pictureID)
                    candidates[1].append(pictureID)

        if searchGeneName:
            candidates[2][0] = 'Gene Name'
            searchCats[2] = '1'
            pictureIDs = []
            pMgdbs = PictureMgdb.objects.filter(locus_full_name__icontains=query[0])
            for pMgdb in pMgdbs:
                pictureID = pMgdb.picture.pk
                if not pictureID in pictureIDs:
                    pictureIDs.append(pictureID)
                    candidates[2].append(pictureID)

        if searchGeneSymbol:
            candidates[3][0] = 'Gene Symbol'
            searchCats[3] = '1'
            pictureIDs = []
            pMgdbs = PictureMgdb.objects.filter(locus_name__icontains=query[0])
            for pMgdb in pMgdbs:
                pictureID = pMgdb.picture.pk
                if not pictureID in pictureIDs:
                    pictureIDs.append(pictureID)
                    candidates[3].append(pictureID)

        if searchGeneID:
            candidates[4][0] = 'Gene ID'
            searchCats[4] = '1'
            pictureIDs = []
            pIDs = PictureGeneID.objects.filter(gene_id__icontains=query[0])
            for pID in pIDs:
                pictureID = pID.picture.pk
                if pictureID not in pictureIDs:
                    pictureIDs.append(pictureID)
                    candidates[4].append(pictureID)

        # Store searching keyword
        if str(request.user) != 'AnonymousUser':
            catSettings = ''.join(searchCats)
            newKeyword, created = iSearchHistory.objects.get_or_create(keyword=query[0], user=request.user)
            if created:
                updateKeyword = iSearchHistory.objects.get(pk__exact=newKeyword.pk)
                updateKeyword.catSettings = catSettings
                updateKeyword.save()
            else:
                newKeyword.catSettings = catSettings
                newKeyword.save()

        formatQuery = ""
        if query:
            formatQuery += 'General Query: "' + ", ".join(query) + '"'


        search = {
            'candidates' : candidates,
            'query' : query[0]
        }

        numSearch += 1
        self.addPageletBinding('center-' + str(numSearch), iSearchPagelet().setSearchParams(search))

        args = {
            'title' : 'Image search',
            'numPagelets' : numSearch
        }
        self.setApplicationLayout('public/iSearch.html', args)

        self.addPageletBinding('footer', FooterPagelet())

'''
    Used for mapping to the url in urls.py
'''
def renderAction(request):
    return Application().render(request)

