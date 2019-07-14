
#### Structure of Directories & Files
```
Notes/
├── api
│   ├── API.py
│   ├── get.py
│   └── post.py
└── Application.py
```


#### Descriptions

Web application for data handling for Image Notes. 

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of Image Notes.

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
    API for Image Notes application

  getNote(request)
    return getAPI.getNote(imageKey)
  addNote(request)
    return postAPI.addNote(notes, pn_id, imageKey)
```


##### api/get.py
```
get.py
  Description:
    Gets Image Notes with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getNote(self, imageKey)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates a new Image Notes with the given parameters

  class PostAPI
    Methods:
      __init__(self, user, fields=None)
      addNote(self, notes, pn_id, imageKey)
        return metadata
```

