from django import template
register = template.Library()

@register.filter(name='sub')
def sub(value, arg):
    if value in ['0', None] or arg in ['0', None]:
        return value
    return value + arg
