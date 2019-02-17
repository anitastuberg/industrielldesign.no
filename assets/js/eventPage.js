let infoBox = $(".signup");
let infoBoxLeftPos = infoBox.position().left;
let scrollAmount = 0;
let newInfoBoxPos;

$(window).scroll(function() {
    if (window.innerWidth >= 600) {
        console.log(window.innerWidth);
        scrollAmount = $(window).scrollTop();
        newInfoBoxPos = infoBoxLeftPos + (scrollAmount * 3);
        console.log(newInfoBoxPos);
        console.log(scrollAmount);
        infoBox.css("left", newInfoBoxPos);
    }
});

$(window).resize(() => {
    if (window.innerWidth < 600) {
        infoBox.css("left", 0);
    } else {
        infoBox.css("left", newInfoBoxPos);
    }
});

let signUpDisplayButton = $("#display-inputs");
let inputFields = $('.input-fields');

signUpDisplayButton.click(function () { 
    inputFields.slideDown("fast");
    $(this).hide();
});
