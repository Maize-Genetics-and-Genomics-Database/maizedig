(function($){
	/**
		JQuery Image Updater Plugin
		Author: Andrew Oberlin
		Date: August 22, 2012
		
		Description: Updates the Images 
		
		Dependencies:
			jQuery 1.7.2 or higher
			jQuery UI 1.8.18 or higher
	**/
	var private_methods = {
		/**
		
		**/
		addPagination: function($self) {
			var settings = $self.data('settings');
			$self.append('<div id="' + settings.organismId + 'Pagination" class="image-pagination"> \
			        <div class="total_pages pagination-control"> \
			        	<span>Total pages: ' + settings.pages  + '</span> \
			        </div> \
					<div class="last pagination-control"> \
		        		<span>&gt;&gt;</span> \
		        	</div> \
					<div class="next pagination-control"> \
			        	<span>&gt;</span> \
			        </div> \
					<div class="move_page pagination-control"> \
			        	<span>GO</span> \
			        </div> \
		        	<div class="numbers_holder" style="float:right;"> \
		        		<input id="move_page_number" type="number" min="1" max="' + settings.pages  + '" value="' + settings.currentPage + '"/> \
		        	</div> \
		        	<div class="previous pagination-control"> \
		        		<span>&lt;</span> \
		        	</div> \
			        <div class="first pagination-control"> \
			        	<span>&lt;&lt;</span> \
			        </div> \
			    </div> \
			');
			    
			$self.find('.last').on('click', function() {
				private_methods.callNewImageSet($self, settings.pages);
			});
			 
		    $self.find('.previous').on('click', function() {
		    	private_methods.callNewImageSet($self, settings.currentPage - 1);
			});
		    
		    $self.find('.next').on('click', function() {
		    	private_methods.callNewImageSet($self, settings.currentPage + 1);
			});
		    
		    $self.find('.first').on('click', function() {
		    	private_methods.callNewImageSet($self, 1);
			});

		    $self.find('.move_page').on('click', function () {
				private_methods.callNewImageSet($self, $self.find('#move_page_number').val());
            });

		},
		/**
			Adds a small template that says no images were found
		**/
		addNoImagesTemplate : function($self) {
			$self.append('<div style="margin-bottom: 10px; text-align: center; color: #3366BB;"> \
				<span> No images were found.</span> \
			</div>');
		},
		/**
			Converts the new page to a range of pictures
		**/
		getRange : function(picsPerPage, page) {
	        var lower =  (page - 1) * picsPerPage;
	        var upper = lower + picsPerPage - 1;
	        return [lower, upper];
	    },
		/**
			Gets a new image set using an ajax call to the change picture 
			application
		**/
		callNewImageSet: function($self, newPage) {
	        var settings = $self.data('settings');
			
			if (newPage < 1) {
	            newPage = 1;
	        }
	        else if (newPage > settings.pages) {
	            newPage = settings.pages;
	        }

	        var range = private_methods.getRange(settings.limit, newPage);
	        $.ajax({
	            url: settings.siteUrl + "api/images/search",
	            type: 'GET',
	            data: {
	                limit: settings.limit,
	                offset: (newPage - 1) * settings.limit,
	                query : settings.query,
                    user : settings.user,
	                iSearchID: settings.iSearchID
	            },
	            dataType: 'json',
	            context: document.body,
	            success: function(data){
	            	var imagesOnPage = 0;
                    var $table = $self.find('table tbody').empty();
                    
                    var $currentRow = $('<tr>').appendTo($table);
                    for (var i = 0; i < data[settings.iSearchID]['images'].length; i++) {
                        if (i % settings.imagesPerRow == 0) {
                            $currentRow = $('<tr>').appendTo($table);
                        }
                        var $currentCell = $('<td>').appendTo($currentRow).addClass('table_cell');

                        private_methods.createNewPictureCell(data[settings.iSearchID]['images'], i, settings, $currentCell);
                        imagesOnPage++;
		            }
                    settings.imagesOnPage = imagesOnPage;
                    settings.currentPage = newPage;

                    // Update current page number on input box
                    $self.find('#move_page_number').val(settings.currentPage);
	            },
	            error: function(jqXHR, textStatus, errorThrown) {
	            	var errorMessage = $.parseJSON(jqXHR.responseText).message;
	                console.log(errorMessage);
	            }
	        });
	    },
	    createNewPictureCell: function (data, index, settings, $currentCell) {
	        var picture = data[index];

	        var $pictureDiv = $('<div>');
	        if (settings.user == 'AnonymousUser')
	        	var $href = $('<a>').attr('href', settings.siteUrl + 'images/editor?imageId=' + picture.id);
	        else
            	var $href = $('<a>').attr('href', settings.siteUrl + 'administration/?dliid=' + picture.id);
	        $href.append($('<img>').attr('src', settings.useActualImages ? picture.url :  picture.thumbnail).width(172).height(130));

	        var $pic_description = '';
            var $pic_description_len = 27;
	        if (picture.description != null)
            	$pic_description = picture.description;
	        else
                $pic_description = 'null';

	        if ($pic_description.length >= $pic_description_len )
	        	$pic_description = $pic_description.substring(0, $pic_description_len) + '...';

	        var $descriptionDiv = $('<div class="description"><span>' + $pic_description + '</span></div>');

	        $currentCell.append($pictureDiv.append($href));
	        $currentCell.append($descriptionDiv);
	    }
	};
	
	var public_methods = {
		/**
			Calls the image updater initialization on a div
		**/
		init: function(options) {
			return this.each(function() {
				var settings = $.extend({
					'staticUrl' : '/static/',
					'siteUrl' : '/',
					'pages' : 1,
					'limit' : 15,
					'currentPage' : 1,
					'totalImages' : 0,
					'imagesPerRow' : 4,
					'query' : '',
                    'user' : '',
					'iSearchID' : -1,
					'useActualImages' : false
				}, options);
				
				$(this).data('settings', settings);
				
				if (settings.totalImages > 0) {
					private_methods.callNewImageSet($(this), settings.currentPage);
					private_methods.addPagination($(this));
				}
				else {
					private_methods.addNoImagesTemplate($(this));
				}
			});
		}
	};

	$.fn.iSearchImageUpdater = function(method) {
		// Method calling logic
		if ( public_methods[method] ) {
			return public_methods[ method ].apply( this, Array.prototype.slice.call( arguments, 1 ));
		} 
		else if ( typeof method === 'object' || ! method ) {
			return public_methods.init.apply( this, arguments );
		} 
		else {
			$.error( 'Method ' +  method + ' does not exist on jQuery.imageUpdater' );
		}  
	};
})( jQuery );

