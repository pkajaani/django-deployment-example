from django import template

register = template.Library()

@register.filter(name='cutIt')
def cutItFunc(value, arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')


#register.filter('cutIt', cutIt)

