from django import template

register=template.Library()

@register.filter()
def replace_char(value,arg):
    return value.replace('h',arg)


@register.filter()
def convert_lower(value):
    return value.lower()

@register.filter()
def counting(value,arg):
    return value.count(arg)

# converting function into a filter
#register.filter('rep',replace_char)