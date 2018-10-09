let infoBox = $(".signup");
let infoBoxLeftPos = infoBox.position().left;
let scrollAmount = 0;
let newInfoBoxPos;
console.log(infoBoxLeftPos);


$(window).scroll(function() {
    scrollAmount = $(window).scrollTop();
    newInfoBoxPos = infoBoxLeftPos + (scrollAmount * 3);
    console.log(newInfoBoxPos);
    console.log(scrollAmount);
    infoBox.css("left", newInfoBoxPos);
});

let signUpDisplayButton = $("#display-inputs");
let inputFields = $('.input-fields');

signUpDisplayButton.click(function () { 
    inputFields.slideDown("fast");
    $(this).hide();
});
