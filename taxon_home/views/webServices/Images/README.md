
#### Structure of Directories & Files
```
Images/
├── api
│   ├── API.py
│   ├── delete.py
│   ├── get.py
│   ├── post.py
│   └── put.py
└── Application.py
```


#### Descriptions

Web application for data handling for Images.

##### Application.py
```
Application.py
  Description:
    Ajax Application for getting the metadata of Images

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
    API for Images application

  getImageMetadata(request)
  createImageMetadata(request)
  editImageMetadata(request)
  deleteImage(request)
    return deleteAPI.deleteImage(imageKey)
```


##### api/get.py
```
get.py
  Description:
    Gets image(s) with given parameters from database

  class GetAPI
    Methods:
      __init__(self, user=None, fields=None)
      getImageMetadata(self, imageKey, isKey=True)
        return metadata
```


##### api/post.py
```
post.py
  Description:
    Creates a new image with the given parameters

  class PostAPI
    Methods:
      __init__(self, user=None, fields=None)
      createImageMetadata(self, image, description, altText, organisms, isKey=True)
        return metadata
  
  handleUpload(upload)
    return (UploadedFile(File(open(filename, 'rb'))), UploadedFile(File(open(thumbnailName, 'rb'))), filename, thumbnailName)
```


##### api/put.py
```
put.py
  Description:
    Updates image with the given parameters

  class PutAPI
    Methods:
      __init__(self, user=None, fields=None)
      editImageMetadata(self, imageKey, description, altText, organisms, isKey=True)
        return metadata
```


##### api/delete.py
```
delete.py
  Description:
    Deletes a image with the given key

  class DeleteAPI
    Methods:
      __init__(self, user=None, fields=None)
      deleteImage(self, imageKey, isKey=True)
```

