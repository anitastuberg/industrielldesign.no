$(function() {
    let editorTextArea = $('#body-text');
    let editorTitle = $('#editor-title');
    let editorIntroduction = $('#editor-introduction');

    let formatBold = $('#format-bold');
    let formatItalic = $('#format-italic');
    let formatSize = $('#format-size');
    let formatImage = $('#format-image');
    let formatLink = $('#format-link');
    let formatQuote = $('#format-quote');
    let formatCode = $('#format-code');
    let formatBullet = $('#format-list-bullet');
    let formatNumber = $('#format-list-number');
    let formatTable = $('#format-table');

    let preview = $('.markdown-preview');

    function previewLoader() {
        marked.setOptions({sanitize: true, tables: true});
        let markedContent = marked(editorTextArea.val());
        preview.html(markedContent);
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
        // A selection is made
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
            editorTextArea.val( currentText.substring(0, caretStart) + text + currentText.substring(caretStart, caretEnd) + textAfter + currentText.substring(caretEnd) );
        }
        
        previewLoader();
    }

    // Event listener for input text
    editorTextArea.bind('input propertychange', previewLoader);
    editorTextArea.bind('input propertychange', previewLoader);

    formatBold.click(() => {
        insertText('bold');
    });
    formatItalic.click( () => {
        insertText('italic');
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
});