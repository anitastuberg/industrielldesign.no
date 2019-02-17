date = new Date();
currentMonth = date.getMonth();
currentYear = date.getFullYear();

let event = $('.event');
let monthDiv = $('.month-div');
let prevMonth = $('.previous-month');
let nextMonth = $('.next-month');
let today = $('.today');
let monthHeader = $('#month');
let yearHeader = $('#year');
let monthYearDiv = $('.month-year');

function getMonthName(monthNum) {
    switch(monthNum) {
        case 0:
            return "januar";
        case 1:
            return "februar";
        case 2:
            return "mars";
        case 3:
            return "april";
        case 4:
            return "mai";
        case 5:
            return "juni";
        case 6:
            return "juli";
        case 7:
            return "august";
        case 8:
            return "september";
        case 9:
            return "oktober";
        case 10:
            return "november";
        case 11:
            return "desember";
    }
}

function updateMonths() {
    monthYearDiv.addClass("changing");
    if (currentMonth == 0) {
        prevMonth.text(getMonthName(11));
    } else {
        prevMonth.text(getMonthName(currentMonth - 1));
    }
    if (currentMonth == 11) {
        nextMonth.text(getMonthName(0));
    } else {
        nextMonth.text(getMonthName(currentMonth + 1));
    }
    monthHeader.text(getMonthName(currentMonth));
    yearHeader.text(currentYear);
    monthDiv.hide(0);
    monthDiv.removeClass("current");
    monthDiv.eq(currentMonth).show().addClass("current");
    // Hides events if next year. Edge case in Leonardo I think
    $('.current a').each(function() {
        if ($(this).data("year") != currentYear) {
            $(this).hide();
        } else {
            $(this).show();
        }
    });
    setTimeout(function() {
        monthYearDiv.removeClass("changing");
    }, 150);
}

function prevMonthfunc() {
    if (currentMonth == 0) {
        currentMonth = 11;
        currentYear -= 1;
    } else {
        currentMonth -= 1;
    }
    updateMonths();
}

function nextMonthfunc() {
    if (currentMonth == 11) {
        currentMonth = 0;
        currentYear += 1;
    } else {
        currentMonth += 1;
    }
    updateMonths();
}

prevMonth.click(function() {
    prevMonthfunc();
});
nextMonth.click(function() {
    nextMonthfunc();
});
today.click(function() {
    currentMonth = date.getMonth();
    currentYear = date.getFullYear();
    updateMonths();
});

$(document).on('keydown', function(e) {
    if (e.which == 37) {
        prevMonthfunc();
    } else if (e.which == 39) {
        nextMonthfunc();
    }
});

updateMonths();
