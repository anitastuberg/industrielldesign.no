const modal = $('.modal');
const scrim = $('.scrim');

const openModal = () => {
    modal.addClass('open');
    scrim.addClass('show');
};

const closeModal = () => {
    modal.removeClass('open');
    scrim.removeClass('show');
};

scrim.click(() => closeModal());