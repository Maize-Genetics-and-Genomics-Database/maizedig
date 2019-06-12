/**
 * Build image attributes data for JSON format
 * @params tagBoard, urlOfImge, imageFile, organisms, uploadDateUser, tagGroups, imageTags, geneLinks
 * @methods
 *   getBase64Image(imgCache)
 *   getFile()
 * @fields
 *   imageFile
 *   imageFilaName
 *   file
 *   obj
 *   objTag
 *   objGeneLink
 *
 * Updated by Kyoung Tak Cho
 * Updated date: Jun 06 20:16:06 CDT 2019
 */
function CachedJsonDataFile(tagBoard, urlOfImage, imageFile, organisms, uploadDateUser, tagGroups, imageTags, geneLinks) {
	this.imageFile = null;
	if (imageFile) {
		this.imageFile = this.getBase64Image(tagBoard.getImageCache());
		this.imageFileName = tagBoard.getImageUrl();
		var lastSlash = this.imageFileName.lastIndexOf("/") + 1;
		this.imageFileName = this.imageFileName.substring(lastSlash);
	}
	
	var file = {
		'MaizeDIGImageMetadata' : {}
	};
	
	var metadata = file['MaizeDIGImageMetadata'];
	
	if (urlOfImage) {
		metadata['urlOfImage'] = tagBoard.getImageUrl();
	}
	
	//if (organisms) {
	//	metadata['organisms'] = tagBoard.getOrganisms();
	//}
	metadata['organisms'] = "Zea mays";

	if (uploadDateUser) {
		metadata['uploadedBy'] = tagBoard.getUploadedBy();
		metadata['uploadDate'] = tagBoard.getUploadDate();
	}
	
	if (tagGroups) {
		var tagGroups = [];
		var groups = tagBoard.getTagGroups();

		for (var i = 0; i < groups.length; i++) {
			var group = groups[i];
			var obj = {};
			
			obj['id'] = group.getKey;
			obj['name'] = group.getName();
			obj['lastModified'] = TaggableUtil.formatDate(group.getLastModified());
			obj['dateCreated'] = TaggableUtil.formatDate(group.getDateCreated());
			
			if (imageTags) {
				var tags = group.getTags();
				var objTags = [];

				for (var j = 0; j < tags.length; j++) {
					var tag = tags[j];
					var objTag = {};
					
					objTag['id'] = tag.getId();
					objTag['color'] = tag.getColor();
					objTag['description'] = tag.getDescription();
					objTag['points'] = tag.getPoints();

					if (geneLinks) {
						var geneLinks = tag.getGeneLinks();
						var objGeneLinks = [];

						for (var k = 0; k < geneLinks.length; k++) {
							var geneLink = geneLinks[k];
							var objGeneLink = {};
							
							objGeneLink['id'] = geneLink.getId();
							objGeneLink['organismId'] = geneLink.getOrganismId();
							objGeneLink['name'] = geneLink.getName();
							objGeneLink['uniquename'] = geneLink.getUniqueName();
							
							objGeneLinks.push(objGeneLink);
						}
						
						objTag['geneLinks'] = objGeneLinks;
					}
					
					objTags.push(objTag);
				}
				
				obj['tags'] = objTags;
			}
			
			tagGroups.push(obj);
		}
		
		metadata['tagGroups'] = tagGroups;
	}

	this.file = file;
};

CachedJsonDataFile.prototype.getBase64Image = function(imgCache) {
	    // Create an empty canvas element
	    var canvas = document.createElement("canvas");
	    canvas.width = imgCache.width;
	    canvas.height = imgCache.height;
	
	    // Copy the image contents to the canvas
	    var ctx = canvas.getContext("2d");
	    ctx.drawImage(imgCache, 0, 0);
	
	    // Get the data-URL formatted image
	    var dataURL = canvas.toDataURL("image/png");
	
	    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
};

CachedJsonDataFile.prototype.getFile = function() {
	var zip = new JSZip();
	zip.file('imageMetadata.json', JSON.stringify(this.file, undefined, 4));
	if (this.imageFile != null) {
		zip.file(this.imageFileName, this.imageFile, { base64: true });
	}

	zip.generateAsync({type:"blob"}).then(function (value) {
		saveAs(value, "imageData.zip");
	});
	return zip;
};