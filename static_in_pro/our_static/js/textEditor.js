$(function() {
    let textEditor = $('.text-editor');
    let textArea = $('.text-editor textarea');
    let formatBold = $('#format-bold');
    let formatItalic = $('#format-italic');
    let formatSize = $('#format-size');
    let formatLink = $('#format-link');
    let formatQuote = $('#format-quote');
    let formatCode = $('#format-code');
    let formatBullet = $('#format-list-bullet');
    let formatNumber = $('#format-list-number');
    let preview = $('.markdown-preview');

    function previewLoader() {
        let markedContent = marked(textArea.val());
        preview.html(markedContent);
    }

    function insertText(text) {
        let caretPos = textArea.selectionStart;
        console.log(caretPos);
        let currentText = textArea.val();
        console.log(currentText);
        textArea.val( currentText.substring(0, caretPos) + text + currentText.substring(caretPos) );
        previewLoader();
    }

    textArea.bind('input propertychange', previewLoader);

    formatBold.click(() => {
        insertText('**Bold**');
    });
    formatItalic.click( () => {
        insertText('*Italic*');
    });
    formatLink.click( () => {
        insertText("[Link-tekst](https://url.com)");
    });
    formatQuote.click( () => {
        insertText('\n> Sitat');
    });
    formatCode.click( () => {
        insertText('`Kodesnutt`');
    });
    formatBullet.click( () => {
        insertText(' - Liste');
    });
    formatNumber.click( () => {
        insertText('1. Liste');
    });
});