function DeleteGeneLinkDialog(pageBlock, organisms, siteUrl) {
    this.block = pageBlock;
    this.submitUrl = siteUrl + 'api/geneLinks';
    
    this.dialog = $('<div />', {
        'class' : 'tagging-dialog',
    });
    
    this.block = pageBlock;
    
    this.title = $('<div />', {
        'class' : 'tagging-dialog-title',
        'text' : 'Delete Gene Link'
    });
    
    this.closeButton = $('<span />', {
        'class' : 'ui-icon ui-icon-circle-close close-button'
    });
    
    this.title.append(this.closeButton);
    
    this.contents = $('<div />', {
        'class' : 'tagging-dialog-contents'
    });
    
    this.table = $('<table />', {
        'class' : 'dialog-table'
    });
    
    this.contents.append(this.table);
    
    this.finalizeUI = $('<div />', {
        'class' : 'tagging-dialog-contents'
    });
    
    this.finalizeBody = $('<div />');
    
    this.deleteGeneLinkButton = $('<button />', {
        'class' : 'tagging-button',
        'style' : 'float: right; margin-right: 10px',
        'text': 'Delete'
    });
    
    this.cancelButton = $('<button />', {
        'class' : 'tagging-button',
        'text': 'Cancel',
        'style' : 'float: right; margin-right: 10px'
    });
    
    this.finalizeBody.append(this.cancelButton);
    this.finalizeBody.append(this.deleteGeneLinkButton);
    this.finalizeBody.css('border-top', '1px solid #CCC');
    this.finalizeBody.css('padding-top', '5px');
    
    this.finalizeUI.append(this.finalizeBody);
    
    this.dialog.append(this.title);
    this.dialog.append(this.contents);
    this.dialog.append(this.finalizeUI);
    
    this.submitCallback = null;
    
    this.deleteGeneLinkButton.on('click', Util.scopeCallback(this, this.onSubmit));
    this.cancelButton.on('click', Util.scopeCallback(this, this.onCancel));
    this.closeButton.on('click', Util.scopeCallback(this, this.onCancel));
    
    $('body').append(this.dialog);
};

DeleteGeneLinkDialog.prototype.onSubmit = function() {
    //alert("test");
    var geneId = this.table.find('input:radio[name=geneLink]:checked').val();
    var organismId = 25;
    if (geneId) {
        var self = this;
        $.ajax({
            url : this.submitUrl,
            type : 'DELETE',
            data : {
                id: geneId
            },
            dataType : 'json',
            success : function(data, textStatus, jqXHR) {
                data.feature.organismId = organismId;
                var geneLink = new GeneLink(geneId, data.feature);
                //self.hide();
                //alert(geneLink.getName() + ' has been deleted!');
            },
            error : function(jqXHR, textStatus, errorThrown) {
                var errorMessage = $.parseJSON(jqXHR.responseText).message;
                alert(errorMessage);
            }
        });
    }
};

DeleteGeneLinkDialog.prototype.onCancel = function() {
    this.hide();
};

DeleteGeneLinkDialog.prototype.hide = function() {
    this.block.hide();
    this.dialog.hide();
};

DeleteGeneLinkDialog.prototype.show = function(tagBoard) {
    var tags = tagBoard.getSelectedTags();
    if ($.isEmptyObject(tags)) {
        var currentTagGroups = tagBoard.getCurrentTagGroups();
        if ($.isEmptyObject(currentTagGroups)) {
            alert("Please select tags by clicking on them or a current tag group.");
        }
        else {
            tags = {};
            $.each(currentTagGroups, function(key, group) {
                $.extend(tags, group.getTags());
            });
        }
    }
    
    if (!$.isEmptyObject(tags)) {
        this.table.empty();
        var tbody = $('<tbody />');
        
        var index = 0;
        $.each(tags, function(id, tag) {
            var geneLinks = tag.getGeneLinks();

            for(var i = 0; i < geneLinks.length; i++) {
                var geneLink = geneLinks[i];

                var newRow = $('<tr />');
            
                var labelCell = $('<td />', {
                    'text' : i == 0 ? 'Select a Gene Link: (' + tag.getDescription() + ')' : ''
                });
            
                var tagCell = $('<td />');
            
                tagCell.append($('<input />', {
                    'value' : geneLink.getId(),
                    'type' : 'radio',
                    'name' : 'geneLink'
                }));
            
                tagCell.append($('<span />', {
                    'text' : geneLink.getName()
                }));
            
                newRow.append(labelCell);
                newRow.append(tagCell);
                tbody.append(newRow);
                index++;
            }
        });
    }
    
    this.tags = tags;
    
    this.table.append(tbody);
    this.block.show();
    this.dialog.show();
};
