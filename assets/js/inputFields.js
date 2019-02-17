$(function() {
    var input = $('input');
    var textarea = $('textarea');
    var select = $('select');

    if (input.length > 0){
        // Check on startup
        input.each(function() {
            if ($( this ).val().length > 0) {
                $( this ).parent(".input-container").addClass("focus");
            }
        });

        input.focus(function() {
            $( this ).parent(".input-container").addClass("focus");
        });
        input.blur(function() {
            if ($( this ).val().length === 0) {
                $( this ).parent(".input-container").removeClass("focus");
            }
        });
    }

    if (textarea.length > 0) {
        textarea.each(function() {
            if ($( this ).val().length > 0) {
                $( this ).parent(".input-container").addClass("focus");
            }
        });
        textarea.focus(function() {
            $( this ).parent(".input-container").addClass("focus");
        });
        
        textarea.blur(function() {
            if ($( this ).val().length === 0) {
                $( this ).parent(".input-container").removeClass("focus");
            }
        });
    }

    if (select.length > 0) {
        select.each(function() {
            if ($( this ).val().length > 0) {
                select.parent(".input-container").addClass("focus");
            }
        });
        if (select.children("option:selected").val().length > 0)  {
            select.parent(".input-container").addClass("focus");
        }
        select.focus(function() {
            $( this ).parent(".input-container").addClass("focus");
        });
        select.change(function() {
            if ($( this ).children("option:selected").val().length === 0)  {
                $( this ).parent(".input-container").removeClass("focus");
            } else {
                $( this ).parent(".input-container").addClass("focus");
            }
        });
    }
});