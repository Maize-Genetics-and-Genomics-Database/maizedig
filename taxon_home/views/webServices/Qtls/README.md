
#### Structure of Directories & Files
```
Qtls/
├── api
│   ├── API.py
│   ├── get.py
│   ├── post.py
└── Application.py
```


#### Descriptions

Web application for data handling for QTLs.

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of QTLs.

  class Application(WebServiceApplicationBase)
    Methods:
      doProcessRender(self, request)
  
  renderAction(request)
    return Application().render(request)
```


##### api/API.py
```
API.py
  Description:
    API for QTLs application

  getQtl(request)
    return getAPI.getQtl(imageKey)
  addQtl(request)
    return postAPI.addQtl(qtl, pq_id, imageKey)
```


##### api/get.py
```
get.py
  Description:
    Gets QTLs with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getQtl(self, imageKey)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates/Updates QTLs with the given parameters

  class PostAPI
    Methods:
      __init__(self, user, fields=None)
      addQtl(self, qtl, pq_id, imageKey)
        return metadata
```


