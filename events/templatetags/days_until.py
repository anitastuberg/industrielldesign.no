from django import template
import datetime

register = template.Library()

@register.filter
def days_until(value):
    """
    Returns number of days between value and today
    Example usage in template:
    {% load days_until %}
    {{ ending_time|daysuntil }}
    """
    today = datetime.date.today()
    try:
        diff = value - today
    except TypeError:
        # convert datetime.datetime to datetime.date
        diff = value.date() - today

    if diff.days >= 1:
        return diff.days
    elif diff.days == 0:
        return 0
    else:
        # Date is in the past; return expired message
        return -1

@register.filter(name='times')
def times(number):
    return range(number)
