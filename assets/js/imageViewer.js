let images = $('.image-viewer-image');
let dots = $('.image-viewer-dot');
let counter = $('.current-count b')
let selectedImageIndex = 0;

dots.click(function () {
    changeImage($(this).index());
});

function changeImage(index) {
    images.each(function () {
        if ($(this).index() < index) {
            $(this).removeClass('right').addClass('left');
        } else if ($(this).index() === index) {
            $(this).removeClass('right left');
        } else if ($(this).index() > index) {
            $(this).removeClass('left').addClass('right');
        }
    });

    dots.removeClass('selected');
    dots.eq(index).addClass('selected');

    selectedImageIndex = index;
    counter.text(('0'+ (index + 1)).slice(-2));
}

function oneStepMove(direction) {
    let i = selectedImageIndex;
    if (direction && i < images.length - 1) {
        i++;
    } else if (!direction && i > 0) {
        i--;
    }
    changeImage(i);
}

$(document).on('keydown', function (e) {
    if (e.which == 37) {
        oneStepMove(false);
    } else if (e.which == 39) {
        oneStepMove(true);
    }
});