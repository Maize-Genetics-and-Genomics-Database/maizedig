
#### Structure of Directories & Files
```
AggregateTagGroups/
├── api/
│   ├── API.py
│   └── get.py
└── Application.py
```


#### Descriptions

Web application for data handling for getting all Tags and GeneLinks given TagGroups.

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata for all Tags and GeneLinks given TagGroups.

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
    API for Aggregate TagGroups application

  getTagGroup(request)
```


##### api/get.py
```
get.py
  Description:
    Gets all Tags and GeneLinks with given TagGroup from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None, unlimited=False)
      getTagGroup(self, tagGroupKey, isKey=True)
        return metadata
```

