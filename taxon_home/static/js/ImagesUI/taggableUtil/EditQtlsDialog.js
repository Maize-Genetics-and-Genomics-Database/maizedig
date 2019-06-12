/**
 * Dialog API for editing QTLs
 *
 * @params pageBlock, siteUrl
 *
 * Modified from EditNotesDialog.js
 * Updated by Kyoung Tak Cho
 * Updated date: Feb 05 23:23:52 CDT 2019
 */
function EditQtlsDialog(pageBlock, siteUrl) {
    this.block = pageBlock;
    this.submitUrl = siteUrl + 'api/qtls';
    
    this.dialog = $('<div />', {
        'class' : 'tagging-dialog',
    });
    
    this.blosdfck = pageBlock;
    
    this.title = $('<div />', {
        'class' : 'tagging-dialog-title',
        'text' : 'Add/Edit QTLs'
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
    
    var qtlsContainer = $('<div />');
    
    this.qtls = $('<textarea />', {
        'id' : 'qtls',
        'name' : 'qtls',
        'cols' : '60',
        'rows' : '10'
    });
    
    var qtlsLabel = $('<span />', {
        'text' : 'QTL',
        'style' : 'margin-right: 10px; margin-left: 10px; margin-bottom: 30px'
    });
    
    qtlsContainer.append(qtlsLabel);
    qtlsContainer.append(this.qtls);
    this.contents.append(qtlsContainer);

    this.finalizeUI = $('<div />', {
        'class' : 'tagging-dialog-contents'
    });
    
    this.finalizeBody = $('<div />');
    
    this.submitQtlsButton = $('<button />', {
        'class' : 'tagging-button',
        'text': ' OK '
    });
    
    this.cancelButton = $('<button />', {
        'class' : 'tagging-button',
        'text': 'Cancel',
        'style' : 'margin-left: 10px'
    });
    
    this.finalizeBody.append(this.submitQtlsButton);
    this.finalizeBody.append(this.cancelButton);
    this.finalizeBody.css('border-top', '1px solid #CCC');
    this.finalizeBody.css('padding-top', '5px');
    
    this.finalizeUI.append(this.finalizeBody);
    
    this.dialog.append(this.title);
    this.dialog.append(this.contents);
    this.dialog.append(this.finalizeUI);
    
    this.submitCallback = null;
    
    this.submitQtlsButton.on('click', Util.scopeCallback(this, this.onSubmit));
    this.cancelButton.on('click', Util.scopeCallback(this, this.onCancel));
    this.closeButton.on('click', Util.scopeCallback(this, this.onCancel));
    
    $('body').append(this.dialog);
};

EditQtlsDialog.prototype.onSubmit = function() {
    var qtl = $.trim(this.qtls.val());
    var pq_id = $.trim(this.qtls.data("qtlsid"));
    var img = document.getElementById("current-editing");
    var pictureID = img.name;

    //if (qtl && pictureID) {
    if (pictureID) {
        var self = this;
        
        $.ajax({
            url : this.submitUrl,
            type : 'POST',
            dataType : 'json',
            data : {
                qtl : qtl,
                pq_id : pq_id,
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

EditQtlsDialog.prototype.onCancel = function() {
    this.hide();
};

EditQtlsDialog.prototype.hide = function() {
    this.block.hide();
    this.dialog.hide();
};

EditQtlsDialog.prototype.show = function(imageMetadata) {

    // Load current QTLs to the <textarea>
    if (imageMetadata)
    {
        $('textarea#qtls').attr({
            'value' : imageMetadata.qtl
        });

        $('textarea#qtls').data({
            'qtlsid' : imageMetadata.qtls_id
        });
    }

    this.block.show();
    this.dialog.show();
};
