
#### Structure of Directories & Files
```
Tags/
├── api
│   ├── API.py
│   ├── delete.py
│   ├── get.py
│   ├── post.py
│   └── put.py
└── Application.py
```

#### Descriptions

Web application for data handling for Tags. 

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of Tags

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
    API for Tags application

  getTag(request)
    return getAPI.getTag(tagKey)
  updateTag(request)
    return putAPI.updateTag(tagKey, points, name, color)
  createTag(request)
    return postAPI.createTag(tagGroupKey, points, name, color)
  deleteTag(request)
    return deleteAPI.deleteTag(tagKey)
```


##### api/get.py
```
get.py
  Description:
    Gets all tags with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getTag(self, tagKey, isKey=True)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates a new tag with the given parameters

  class PostAPI
    Methods:
      __init__(self, user, fields=None)
      createTag(self, tagGroupKey, points, name, color, isKey=True)
        return metadata
```


##### api/put.py
```
put.py
  Description:
    Updates tag with the given parameters

  class PutAPI
    Methods:
      __init__(self, user=None, fields=None)
      updateTag(self, tagKey, points=None, name=None, color=None, isKey=True)
        return metadata
```


##### api/delete.py
```
delete.py
  Description:
    Deletes a tag with the given key

  class DeleteAPI
    Methods:
      __init__(self, user=None, fields=None)
      deleteTag(self, tagKey, isKey=True)
```




