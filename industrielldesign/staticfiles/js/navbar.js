let hamburger = $('#hamburger');
let navigation = $('#main-navigation');

hamburger.click(() => {
  console.log('Hamburger clicked');
  hamburger.toggleClass('closed');
});