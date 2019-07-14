
#### Structure of Directories & Files
```
SearchImages/
├── api
│   ├── API.py
│   └── get.py
└── Application.py
```


#### Descriptions

Web application for data handling for Image Notes. 

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata for Image search.

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
    API for Image search application

  getImageMetadata(request)
```


##### api/get.py
```
get.py
  Description:
    Gets Image search with given parameters from database

  class GetAPI
    Methods:
      __init__(self, limit=10, offset=0, user=None, fields=None, unlimited=False)
      getImageMetadata(self)
        return metadata
      getImageMetadataForiSearch(self, query)
        return metadata
      getImageMetadataByOrganism(self, organismId)
        return metadata
```

