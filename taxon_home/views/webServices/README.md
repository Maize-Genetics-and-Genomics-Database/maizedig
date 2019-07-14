
#### Structure of Directories & Files
```
webServices/
├── AggregateTagGroups/             # Ajax Application for getting the metadata of Tag groups
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── AggregateTagGroupsSearch/       # Ajax Application for getting the metadata for Tag group search
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── GeneLinks/                      # Ajax Application for getting the metadata of GeneLinks
│   ├── api/
│   │   ├── API.py
│   │   ├── delete.py
│   │   ├── get.py
│   │   └── post.py
│   └── Application.py
├── Images/                         # Ajax Application for getting the metadata abourt an image
│   ├── api/
│   │   ├── API.py
│   │   ├── delete.py
│   │   ├── get.py
│   │   ├── post.py
│   │   └── put.py
│   └── Application.py
├── Notes/                          # Ajax Application for handling for Image Notes data
│   ├── api/
│   │   ├── API.py
│   │   ├── get.py
│   │   └── post.py
│   └── Application.py
├── Qtls/                           # Ajax Application for handling QTL data
│   ├── api/
│   │   ├── API.py
│   │   ├── get.py
│   │   └── post.py
│   └── Application.py
├── SearchGeneLinks/                # Ajax Application for getting the metadata for GeneLinks search
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── SearchImages/                   # Ajax Application for getting the metadata for image search
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── SearchOrganisms/                # Ajax Application for getting the metadata for organisms search - NOT USED
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── SearchTagGroups/                # Ajax Application for getting the metadata for Tag groups search
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── SearchTags/                     # Ajax Application for getting the metadata for Tags search
│   ├── api/
│   │   ├── API.py
│   │   └── get.py
│   └── Application.py
├── TagGroups/                      # Ajax Application for getting the metadata of TagGroups
│   ├── api/
│   │   ├── API.py
│   │   ├── delete.py
│   │   ├── get.py
│   │   ├── post.py
│   │   └── put.py
│   └── Application.py
└── Tags/                           # Ajax Application for getting the metadata of Tags
    ├── api/
    │   ├── API.py
    │   ├── delete.py
    │   ├── get.py
    │   ├── post.py
    │   └── put.py
    └── Application.py
```

#### Descriptions

`webServices/` directory contains applications for data handling between Django web application and database. 
The basic structure of a webService application is belows:

```
webService_application/
├── api/
│   ├── API.py              # Provides interface for application
│   ├── get.py              # Gets data from database
│   ├── put.py              # Updates data 
│   ├── post.py             # Adds data into database
│   └── delete.py           # Delete data
└── Application.py          # Applicaton 
```


