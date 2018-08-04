modalContent = $('.modal-content');
scrim = $('.scrim');

function openModal() {
    modalContent.slideDown();
    scrim.fadeIn();
}

function closeModal() {
    modalContent.slideUp();
    scrim.fadeOut();
}