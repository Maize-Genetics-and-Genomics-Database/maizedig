
#### Structure of Key Directories & Files
```
js/                                     # Java Script (JQuery) for data handling
├── ImagesUI/                           # Image data handler using JQuery 
│   ├── tagViewerUtil/                  # Tagging Tool for Image Viewer (Public mode)
│   │   ├── DrawingAPI.js               # API for drawing on the drawing board
│   │   └── TaggerUI.js                 # Tagger UI and menu
│   ├── tagViewingUI/                   # UI for displaying Tag/GeneLink information
│   │   ├── DownloadImageDataDialog.js  # Download image attribute data
│   │   ├── GeneLink.js                 # Handle Gene Link data
│   │   ├── TagBoard.js                 # Drawing object for the Tag Board
│   │   ├── TaggableUtil.js             # Static utility methods for canvases
│   │   ├── TagGroup.js                 # Handle Tag Group data
│   │   └── Tag.js                      # Handle Tag data
│   ├── taggableUtil/                   # Tagging Tool menu for Workbench (Admin mode)
│   │   ├── DeleteGeneLinkDialog.js     # Dialog API for Delete Gene Link
│   │   ├── DrawingAPI.js               # API for drawing on the drawing board
│   │   ├── DrawingBoard.js             # DrawingBoard object for drawing the tags
│   │   ├── EditNotesDialog.js          # Dialog API for Add/Edit image notes
│   │   ├── EditQtlsDialog.js           # Dialog API for Add/Edit QTLs information
│   │   ├── NewGeneLinkDialog.js        # Dialog API for Add Gene Link
│   │   ├── NewTagGroupDialog.js        # Dialog API for Add Tag Group
│   │   ├── SaveTagDialog.js            # Dialog API for saving Tag
│   │   ├── TaggerUI.js                 # Creates a tagging application that links to the database using Ajax
│   │   └── TaggingMenu.js              # Tagging Menu handler
│   ├── tagViewer.js                    # JQuery TagViewer Plugin
│   ├── taggable.js                     # JQuery Taggable Plugin
│   └── zoomable.js                     # JQuery Zoomable Plugin
└── imageUpdater/
    ├── imageUpdater.js                 # Build Image List for Image menu
    └── iSearchImageUpdater.js          # Build Image list (JQuery) for Image Search results page
```

`ImageUI/` and `imageUpdater/` are key directories in `js/`.
`ImageUI/` has `tagViewingUI/`, `tagViewerUtil/`, and `taggableUtil/`. 
The `tagViewingUI/` contains data handlers for image viewer/editor (for both public and admin modes). 
And there are two utils: `tagViewerUtil` and `taggableUtil`. 
The `tagViewerUtil` is for image viewer (public mode only) and 
the `taggableUtil` is for image editor (admin mode). 


