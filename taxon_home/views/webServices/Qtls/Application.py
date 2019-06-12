'''
	Ajax Application for handling QTL data

	Author: Kyoung Tak Cho
	Creaded Date: December 21, 2018
	Last updated: January 10, 2019
'''
from renderEngine.AjaxApplicationBase import WebServiceApplicationBase
from renderEngine.WebServiceObject import WebServiceObject
import taxon_home.views.util.ErrorConstants as Errors
from django.views.decorators.csrf import csrf_exempt
import api.API as API

class Application(WebServiceApplicationBase):
    def doProcessRender(self, request):
        renderObj = WebServiceObject()
        try:
            if request.method == "GET":
                renderObj = API.getQtl(request)
            elif request.method == "POST":
                print 'test at doProcessRender()'
                renderObj = API.addQtl(request)
            #elif request.method == "PUT":
            #    renderObj = API.updateQtl(request)
            #elif request.method == "DELETE":
            #    renderObj = API.deleteQtl(request)
            else:
                renderObj.setError(Errors.INVALID_METHOD.setCustom(request.method))
        except Errors.WebServiceException as e:
            renderObj.setError(e)

        self.setJsonObject(renderObj.getObject())
        self.setStatus(renderObj.getCode())


'''
	Used for mapping to the url in urls.py
'''
@csrf_exempt
def renderAction(request):
    return Application().render(request)

