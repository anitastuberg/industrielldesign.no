let hamburger = $('#hamburger');
let navigation = $('#main-navigation');
let close = $('#close-nav');
let dropdowns = $('.nav-item.dropdown span');

hamburger.click(function() {
  hamburger.removeClass('closed')
});

close.click(function() {
  hamburger.addClass('closed');
});

dropdowns.click(function() {
  $(this).parent().toggleClass('open');
});