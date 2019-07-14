
#### Structure of Directories & Files
```
taxon_home/
├── media/              # Image files stored here
├── static/             # Static files such as CSS, Java Script, etc.
├── templates/          # HTML templates for page layouts
├── templatetags/
├── views/              # Applications, pagelets, util, and web services
├── admin.py            # Register models for admin page (Workbench)
├── models.py           # Data handlers for Database
├── routers.py          # A router to control all database operations on models in the contrib.auth application
└── tests.py
```

'**taxon_home**' is main working directory in this project 
and actual applications and web development source codes are placed under the '**views**' directory. 


##### admin.py
```
admin.py
  Description:
    register models for admin page (Workbench)
    
  admin.site.register(Picture)
  admin.site.register(TagGroup)
  admin.site.register(Tag)
  admin.site.register(TagColor)
  admin.site.register(TagPoint)
  admin.site.register(BlastUpload)
  admin.site.register(Landmark)
  admin.site.register(PictureDefinitionTag)
  admin.site.register(Organism)
  admin.site.register(RecentlyViewedPicture)
  admin.site.register(GeneLink)
```


##### models.py

Django provides *models* concept for easy/simple way to handle database query. 
All tables used in MaizeDIG are defined in models.py and the key models are shown below:

```
Key models:
  Picture                   # Image data
  TagGroup                  # Tag group
  Tag                       # Tag information
  TagPoint                  # Tagged area information of image
  GeneLink                  # GeneLink information
  Feature                   # Genotypic data
  PictureNotes              # Image Notes
  PictureQtl                # QTLs
  PictureMgdb               # Relationship between MaizeDIG DB and MaizeGDB DB
  iSearchHistory            # Image Search history
  RecentlyViewedPicture     # Recently viewed images
```


##### routers.py
```
routers.py
  Description:
    A router to control all database operations on models in
    the contrib.auth application

  class DBRouter
    Methods:
      db_for_read
      db_for_write
      allow_syncdb
```


##### tests.py

This file demonstrates writing tests using the unittest module. 
These will pass when you run `manage.py test`.


