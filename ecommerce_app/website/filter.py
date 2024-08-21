from django import template

register = template.Library()

@register.filter
def truncate_title(title, length=5):
    if len(title) > length:
        return title[:length] + '...'
    return title
