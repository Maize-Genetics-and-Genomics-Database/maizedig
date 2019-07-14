
#### Structure of Directories & Files
```
views/
├── applications/                       # Applications for layout handler
│   ├── admin/                          # Admin mode
│   │   └── Customize/                  # Admin page customize page handler - NOT USED
│   ├── public/                         # Public mode
│   │   ├── AdvancedSearch/             # NOT USED
│   │   ├── Blast/
│   │   ├── EditImage/
│   │   ├── GBrowse/
│   │   ├── Home/
│   │   ├── Images/                     # Image Viewer layout handler
│   │   ├── iSearch/                    # Image Search layout handler
│   │   ├── Login/
│   │   ├── Logout/
│   │   ├── Media/
│   │   └── Search/                     # NOT USED
│   └── registered/
│       ├── Administration/             # Admin page layout handler
│       ├── ImageUploader/              # Image manual uploader
│       └── TGManager/                  # NOT USED
├── pagelets/                           # Web page UI applications
│   ├── admin/                          # Admin mode
│   │   ├── CustomizePagelet.py         # Pagelet for the customization of the website
│   │   └── ImageEditorPagelet.py       # Pagelet for the Image Editor for admin mode
│   ├── public/                         # Public mode
│   │   ├── AdvancedSearchPagelet.py    # NOT USED
│   │   ├── BlastPagelet.py
│   │   ├── BlastResultsPagelet.py
│   │   ├── FooterPagelet.py
│   │   ├── GBrowsePagelet.py           # NOT USED
│   │   ├── GBrowseSearchPagelet.py     # NOT USED
│   │   ├── HomePagelet.py              # Pagelet for the main page (Home)
│   │   ├── ImageEditorPagelet.py       # Pagelet for the Image Editor for public mode
│   │   ├── ImageSearchPagelet.py       # Pagelet for the Search page (NOT USED)
│   │   ├── ImagesPagelet.py            # Pagelet for the Image page
│   │   ├── iSearchPagelet.py           # Pagelet for the Image Search page
│   │   └── NavBarPagelet.py            # Pagelet for the Navigation Bar (Public mode)
│   └── registered/                     # Admin mode
│       ├── ImageUploaderPagelet.py     # Pagelet for the Manual Image Upload page
│       ├── NavBarPagelet.py            # Pagelet for the Navigation Bar (Admin mode)
│       ├── TGManagerPagelet.py
│       └── WorkbenchPagelet.py         # Pagelet for the Workbench page (Admin mode)
├── util/
│   ├── ErrorConstants.py
│   └── Util.py
└── webServices/                        # Web service (Ajax) applications
    ├── AggregateTagGroups/
    ├── AggregateTagGroupsSearch/
    ├── GeneLinks/                      # Ajax application for GeneLinks data
    ├── Images/                         # Ajax application for images data
    ├── Login/
    ├── Notes/                          # Ajax application for image notes
    ├── Qtls/                           # Ajax application for QTLs
    ├── SearchGeneLinks/
    ├── SearchImages/                   # Ajax application for Image search
    ├── SearchOrganisms/
    ├── SearchTagGroups/
    ├── SearchTags/
    ├── TagGroups/                      # Ajax application for Tag groups
    └── Tags/                           # Ajax application for Tags
```



