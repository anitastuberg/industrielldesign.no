let hamburger = $('#hamburger');
let navigation = $('#main-navigation');
let close = $('#close-nav')

hamburger.click(function() {
  hamburger.removeClass('closed')
});

close.click(function() {
  hamburger.addClass('closed');
});