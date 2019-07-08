$(function() {
    let editorTitle = $('#id_title');
    let editorIntroduction = $('#id_introduction');
    let editorTextArea = $('#id_body_text');

    let formatBold = $('#format-bold');
    let formatItalic = $('#format-italic');
    let formatTitle = $('#format-title');
    let formatImage = $('#format-image');
    let formatLink = $('#format-link');
    let formatQuote = $('#format-quote');
    let formatCode = $('#format-code');
    let formatBullet = $('#format-list-bullet');
    let formatNumber = $('#format-list-number');
    let formatTable = $('#format-table');

    let title = $('.article__title');
    let introductuon = $('.article__introduction');
    let preview = $('.markdown-preview');

    function previewLoader() {
        marked.setOptions({sanitize: true, tables: true, baseUrl: "../"});
        let markedContent = marked(editorTextArea.val());
        preview.html(markedContent);
        title.text(editorTitle.val());
        introductuon.text(editorIntroduction.val());
    }

    function insertText(type) {
        let caretStart = editorTextArea.prop("selectionStart");
        let caretEnd = editorTextArea.prop("selectionEnd");
        let currentText = editorTextArea.val();
        let text;
        let textAfter;

        // Not a selection
        if (caretStart === caretEnd) {
            switch(type) {
                case "bold":
                    text = "**Bold**";
                    break;
                case "italic":
                    text = "*Italic*";
                    break;
                case 'title':
                    text = "\n# Mellomtittel";
                    break;
                case "image":
                    text = '![alt text](https://url.com/image.png)';
                    break;
                case "link":
                    text = "[Link tekst](https://url.com)";
                    break;
                case "quote":
                    text = "\n> Sitat";
                    break;
                case "code":
                    text = "`code`";
                    break;
                case "ul":
                    text = "\n - liste";
                    break;
                case "ol":
                    text = "\n1. liste";
                    break;
                case "table":
                    text = "\n| Tittel | Tittel | Tittel |\n" +
                        "| --- | --- | --- |\n" +
                        "| Tekst | Tekst | Tekst |";
            }
            editorTextArea.val( currentText.substring(0, caretStart) + text + currentText.substring(caretStart) );
        } 
        // Else = selection not just caret
        else {
            switch(type) {
                case "bold":
                    text = "**";
                    textAfter = "**";
                    break;
                case "italic":
                    text = "*";
                    textAfter = "*";
                    break;
                case 'title':
                    text ="\n# ";
                    textAfter = "";
                    break;
                case "image":
                    text = '![';
                    textAfter = "](https://url.com/image.png)";
                    break;
                case "link":
                    text = "[";
                    textAfter = "](https://url.com)";
                    break;
                case "quote":
                    text = "\n> ";
                    textAfter = "";
                    break;
                case "code":
                    text = "`";
                    textAfter = "`";
                    break;
                case "ul":
                    text = "\n - ";
                    textAfter = "";
                    break;
                case "ol":
                    text = "\n1. ";
                    textAfter = "";
                    break;
                case "table":
                    text = "\n| Tittel | Tittel | Tittel |\n" +
                    "| --- | --- | --- |\n" +
                    "| Tekst | Tekst | Tekst |";
                    textAfter = "";
            }
            // Recreates the text with markdown at cursor/selection
            editorTextArea.val( currentText.substring(0, caretStart) + text + currentText.substring(caretStart, caretEnd) + textAfter + currentText.substring(caretEnd) );
        }
        
        // Load preview again when inserting text with buttons
        previewLoader();

        // Triggers the autoexpanding textarea in autoExpandingTextArea.js
        $('textarea').trigger('input');
    }

    // Event listener for input text in all input-fields
    editorTextArea.bind('input propertychange', previewLoader);
    editorTitle.bind('input propertychange', previewLoader);
    editorIntroduction.bind('input propertychange', previewLoader);

    // Autoresizes textareas to be as tall as its content
    // Uses autoExpandingTextArea.js
    // $(".autoResize").autoResize();

    // Creating eventlisteners for all format buttons.
    // Sends a string to insertText which is used in a switch statement.
    formatBold.click(() => {
        insertText('bold');
    });
    formatItalic.click( () => {
        insertText('italic');
    });
    formatTitle.click( () => {
        insertText('title');
    });
    formatImage.click( () => {
        insertText("image");
    });
    formatLink.click( () => {
        insertText("link");
    });
    formatQuote.click( () => {
        insertText('quote');
    });
    formatCode.click( () => {
        insertText('code');
    });
    formatBullet.click( () => {
        insertText('ul');
    });
    formatNumber.click( () => {
        insertText('ol');
    });
    formatTable.click( () => {
        insertText('table');
    });

    // Load preview on refresh
    previewLoader();
});