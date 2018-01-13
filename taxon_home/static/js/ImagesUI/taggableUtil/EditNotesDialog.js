function EditNotesDialog(pageBlock, siteUrl) {
    this.block = pageBlock;
    this.submitUrl = siteUrl + 'api/notes';
    
    this.dialog = $('<div />', {
        'class' : 'tagging-dialog',
    });
    
    this.block = pageBlock;
    
    this.title = $('<div />', {
        'class' : 'tagging-dialog-title',
        'text' : 'Add/Edit Image Notes'
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
    
    var notesContainer = $('<div />');
    
    this.notes = $('<textarea />', {
        'id' : 'notes',
        'name' : 'notes',
        'cols' : '60',
        'rows' : '10'
    });
    
    var notesLabel = $('<span />', {
        'text' : 'Notes',
        'style' : 'margin-right: 10px; margin-left: 10px; margin-bottom: 30px'
    });
    
    notesContainer.append(notesLabel);
    notesContainer.append(this.notes);
    this.contents.append(notesContainer);

    this.finalizeUI = $('<div />', {
        'class' : 'tagging-dialog-contents'
    });
    
    this.finalizeBody = $('<div />');
    
    this.submitNotesButton = $('<button />', {
        'class' : 'tagging-button',
        'text': ' OK '
    });
    
    this.cancelButton = $('<button />', {
        'class' : 'tagging-button',
        'text': 'Cancel',
        'style' : 'margin-left: 10px'
    });
    
    this.finalizeBody.append(this.submitNotesButton);
    this.finalizeBody.append(this.cancelButton);
    this.finalizeBody.css('border-top', '1px solid #CCC');
    this.finalizeBody.css('padding-top', '5px');
    
    this.finalizeUI.append(this.finalizeBody);
    
    this.dialog.append(this.title);
    this.dialog.append(this.contents);
    this.dialog.append(this.finalizeUI);
    
    this.submitCallback = null;
    
    this.submitNotesButton.on('click', Util.scopeCallback(this, this.onSubmit));
    this.cancelButton.on('click', Util.scopeCallback(this, this.onCancel));
    this.closeButton.on('click', Util.scopeCallback(this, this.onCancel));
    
    $('body').append(this.dialog);
};

EditNotesDialog.prototype.onSubmit = function() {
    var notes = $.trim(this.notes.val());
    var pn_id = $.trim(this.notes.data("notesid"));
    var img = document.getElementById("current-editing");
    var pictureID = img.name;

    if (notes && pictureID) {
        var self = this;
        
        $.ajax({
            url : this.submitUrl,
            type : 'POST',
            dataType : 'json',
            data : {
                notes : notes,
                pn_id : pn_id,
                pictureID : pictureID
            },
            success : function(data, textStatus, jqXHR) {
                self.hide();
                location.href = '/administration/?dliid=' + pictureID;
            },
            error : function(jqXHR, textStatus, errorThrown) {
                var errorMessage = $.parseJSON(jqXHR.responseText).message;
                alert(errorMessage);
            }
        });
    }
};

EditNotesDialog.prototype.onCancel = function() {
    this.hide();
};

EditNotesDialog.prototype.hide = function() {
    this.block.hide();
    this.dialog.hide();
};

EditNotesDialog.prototype.show = function(imageMetadata) {

    // Load current notes to the <textarea>
    if (imageMetadata)
    {
        $('textarea#notes').attr({
            'value' : imageMetadata.notes
        });
        //$('textarea#notes').val(imageMetadata.notes);

        $('textarea#notes').data({
            'notesid' : imageMetadata.notes_id
        });
    }

    this.block.show();
    this.dialog.show();
};
