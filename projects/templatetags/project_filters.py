from django import template

register = template.Library()


@register.filter(name='get_first_project_image_url')
def get_first_project_image_url(images):
    images = list(images)
    if len(images):
        return list(images)[0].image.url
    else:
        return "Unknown"
