$(function () {


  let bar = $('#bar');
  let listElement = $('#main-navigation ul li');
  let selected = $('#main-navigation ul .selected');

  if (!selected.length) {
    bar.hide();
  }

  if (selected.length) {
    var selectedWidth = selected.width();
    var selectedPosition = selected.position();
  
    bar.css({
      'width': selectedWidth,
      'left': selectedPosition.left
    });
    bar.addClass('color' + selected.index());
  }

  function hoverIn() {
    if (!selected.length) {
      bar.show();
    }
    let color, listWidth, listIndex;
    listWidth = $(this).width();
    listIndex = $(this).index();
    bar.removeClass();
    bar.addClass('color' + listIndex);
    bar.css({
      'width': listWidth,
      'left': $(this).position().left
    });
  }

  function hoverOut() {
    if (!selected.length) {
      bar.hide();
      bar.css({
        'width': '0',
        'left': '0'
      });
    } else {

      bar.removeClass();
      bar.css({
        'width': selectedWidth,
        'left': selectedPosition.left
      });
      bar.addClass('color' + selected.index());
    }

  }

  listElement.hover(hoverIn, hoverOut);

  secondListElement = $('#second ul li');

});