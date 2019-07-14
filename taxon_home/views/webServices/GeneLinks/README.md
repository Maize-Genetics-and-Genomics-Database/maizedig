
#### Structure of Directories & Files
```
GeneLinks/
├── api
│   ├── API.py
│   ├── delete.py
│   ├── get.py
│   └── post.py
└── Application.py
```

#### Descriptions

Web application for data handling for GeneLinks


##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of GeneLinks

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
    API for GeneLinks application

  getGeneLink(request)
    return getAPI.getGeneLink(geneLinkKey)
  createGeneLink(request)
    return postAPI.createGeneLink(tagId, name, allele, organismId)
  deleteGeneLink(request)
    return deleteAPI.deleteGeneLink(geneLinkKey)
```


##### api/get.py
```
get.py
  Description:
    Gets all GeneLinks with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getGeneLink(self, geneLinkKey, isKey=True)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates a new GeneLink with the given parameters

  class PostAPI
    Methods:
      __init__(self, user, fields=None)
      createGeneLink(self, tagKey, name=None,  allele=None, organismId=None, isKey=True)
        return metadata
```


##### api/delete.py
```
delete.py
  Description:
    Deletes a GeneLink with the given key

  class DeleteAPI
    Methods:
      __init__(self, user=None, fields=None)
      deleteGeneLink(self, geneLinkKey, isKey=True)
```






















