
#### Structure of Directories & Files
```
AggregateTagGroupsSearch/
├── api/
│   ├── API.py
│   └── get.py
└── Application.py
```


#### Descriptions

Web application for data handling for getting all Tags and GeneLinks given Image.

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata for all Tags and GeneLinks given Image.

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
    API for Aggregate TagGroups for given Image

  getAggregateTagGroups(request)
    ...
    if imageKey:
      return getAPI.getAggregateTagGroupsByImage(imageKey)
    else:
      return getAPI.getAggregateTagGroups()
```


##### api/get.py
```
get.py
  Description:
    Gets all Tags and GeneLinks with given Image from database

  class GetAPI
    Methods:
      __init__(self, limit=10, offset=0, user=None, fields=None, unlimited=False)
      getAggregateTagGroupsByImage(self, imageKey, isKey=True)
        return metadata
      getAggregateTagGroups(self)
        return metadata
```

