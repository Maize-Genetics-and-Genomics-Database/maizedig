
#### Structure of Directories & Files
```
TagGroups/
├── api
│   ├── API.py
│   ├── delete.py
│   ├── get.py
│   ├── post.py
│   └── put.py
└── Application.py
```

#### Descriptions

Web application for data handling for TagGroups. 

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of TagGroups

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
    API for TagGroups application

  getTagGroup(request)
    return getAPI.getTagGroup(tagGroupKey)
  updateTagGroup(request)
    return putAPI.updateTagGroup(tagGroupKey, name)
  createTagGroup(request)
    return postAPI.createTagGroup(imageKey, name)
  deleteTagGroup(request)
    return deleteAPI.deleteTagGroup(tagGroupKey)
```


##### api/get.py
```
get.py
  Description:
    Gets all TagGroups with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getTagGroup(self, tagGroupKey, isKey=True)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates new TagGroups with the given parameters

  class PostAPI
    Methods:
      __init__(self, user, fields=None)
      createTagGroup(self, imageKey, name, isKey=True)
        return metadata
```


##### api/put.py
```
put.py
  Description:
    Updates TagGroups with the given parameters

  class PutAPI
    Methods:
      __init__(self, user=None, fields=None)
      updateTagGroup(self, tagGroupKey, name=None, isKey=True)
        return metadata
```


##### api/delete.py
```
delete.py
  Description:
    Deletes TagGroups with the given key

  class DeleteAPI
    Methods:
      __init__(self, user=None, fields=None)
      deleteTagGroup(self, tagGroupKey, isKey=True)
        return metadata
```
