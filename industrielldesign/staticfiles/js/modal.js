modalContent = $('.modal');
scrim = $('.scrim');

function openModal() {
    modalContent.show();
    scrim.fadeIn();
}

function closeModal() {
    modalContent.hide();
    scrim.fadeOut();
}

scrim.click(closeModal);