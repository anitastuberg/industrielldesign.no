from django import template
from datetime import datetime, timezone

register = template.Library()

# @register.filter
# def days_until(value):
#     """
#     Returns number of days between value and today
#     Example usage in template:
#     {% load days_until %}
#     {{ ending_time|daysuntil }}
#     """
#     today = datetime.date.today()
#     try:
#         diff = value - today
#     except TypeError:
#         # convert datetime.datetime to datetime.date
#         diff = value.date() - today

#     if diff.days >= 1:
#         return diff.days
#     elif diff.days == 0:
#         return 0
#     else:
#         # Date is in the past; return expired message
#         return -1

@register.filter
def days_until(value):
    now = datetime.now(timezone.utc)
    diff = value - now
    return diff

@register.filter(name='times')
def times(number):
    return range(number)
