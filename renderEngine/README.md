
#### Directory & File structure

```
renderEngine/
├── __init__.py
├── AdminApplicationBase.py
├── AjaxAdminApplicationBase.py
├── AjaxApplicationBase.py
├── AjaxRegisteredApplicationBase.py
├── ApplicationBase.py
├── PageletBase.py
├── RegisteredApplicationBase.py
├── RenderEngine.py
├── WebServiceException.py
└── WebServiceObject.py
```

#### Description

In this directory, rendering modules for Django are defined 
and the detail structure for each class is follows: 


##### AdminApplicationBase.py

```
AdminApplicationBase.py
  Description:
    Used in junction with the rendering engine to render a page that should only
    be accessed by an administrator
    
  class AdminApplicationBase(ApplicationBase)
    Methods:
      render
```


##### AjaxAdminApplicationBase.py

```
AjaxAdminApplicationBase.py
  Description:
    This application uses the renderEngine to render pure JSON instead
    of a page. To be used in junction with Ajax

  class AjaxAdminApplicationBase(AjaxApplicationBase)
    Methods:
      render

  renderAction(request)
```


##### AjaxApplicationBase.py

```
AjaxApplicationBase.py
  Description:
    This application uses the renderEngine to render pure JSON instead
    of a page. To be used in junction with Ajax

  class AjaxApplicationBase
    Methods:
      __init__
      setJsonObject
      setStatus
      doProcessRender
      render
      coerce_delete_post
      coerce_put_post
      throttle
    Fields:
      extra
      renderEngine
  
  class WebServiceApplicationBase(AjaxApplicationBase)
    methods:
      setJsonObject
      getJsonObject
  
  renderAction(request)
```


##### AjaxRegisteredApplicationBase.py
```
AjaxRegisteredApplicationBase.py
  Description:
    This application uses the renderEngine to render pure JSON instead
    of a page. To be used in junction with Ajax
  
  class AjaxRegisteredApplicationBase(AjaxApplicationBase)
    Methods:
      render
      
  renderAction(request)
```


##### ApplicationBase.py
```
ApplicationBase.py
  Description:
    Used in junction with the rendering engine to render a page
  
  class ApplicationBase
    Methods:
      __init__
      setApplicationLayout
      setStatus
      addPageletBinding
      doProcessRender
      render
    Fields:
      renderEngine
  
  renderAction(request)
```


##### PageletBase.py
```
PageletBase.py
  Description:
    Pagelet Object for Django
  
  class PageletBase
    Methods:
      __init__
      doProcessRender
      setLayout
      getLayout
      render
    Fields:
      pageletLayout
```


##### RegisteredApplicationBase.py
```
RegisteredApplicationBase.py
  Description:
    Used in junction with the rendering engine to render a page that should only
    be accessed by an administrator
  
  class RegisteredApplicationBase(ApplicationBase)
    Methods:
      render
```


##### RenderEngine.py
```
RenderEngine.py
  Description:
    Render Engine for Django
  
  class RenderEngine
    Methods:
      setStatus
      setApplicationLayout
      getApplicationLayout
      addPageletBinding
      renderPagelet
      render
      renderJson
    Fields:
      applicationArgs
      applicationLayout
      layoutDir
      pageletDir
      pageletMap
      status
```


##### WebServiceException.py
```
WebServiceException.py
  Description:
    Exception handling for web service
  
  class WebServiceException(Exception)
    Methods:
      __init__
      getMessage
      getCode
    Fields:
      code
      message

  class CustomWebServiceException(WebServiceException)
    Methods:
      setCustom
      getMessage
    Fields:
      custom
```


##### WebServiceObject.py
```
WebServiceObject.py
  Description:
    Handle for web service object

  class WebServiceObject
    Methods:
      __init__
      put
      setError
      isError
      getErrorMessage
      getCode
      getError
      getObject
      allowsField
      limitFields
      setObject
    Fields:
      error
      errorObj
      fields
      obj

  class WebServiceArray(WebServiceObject)
    Methods:
      __init__
      put
    Fields:
      error
      errorObj
      fields
      obj

  LimitDict(fields, initialDict)
```


