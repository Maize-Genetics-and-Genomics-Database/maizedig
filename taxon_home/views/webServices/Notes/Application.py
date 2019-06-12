'''
	Ajax Application for handling Image Notes data

	Author: Kyoung Tak Cho
	Date: Oct. 23, 2017
    Last Updated: Oct 24 21:48:23 CDT 2017
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
                renderObj = API.getNote(request)
            elif request.method == "POST":
                renderObj = API.addNote(request)
            #elif request.method == "PUT":
            #    renderObj = API.updateNote(request)
            #elif request.method == "DELETE":
            #    renderObj = API.deleteNote(request)
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

