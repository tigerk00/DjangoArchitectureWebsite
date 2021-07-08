from django import template

register = template.Library()

@register.filter(name='mod_two')
def mod_two(value):
    return int(value)%2


@register.filter(name='get_class')
def get_class(value):
  return value.__class__.__name__


@register.filter(name='cut')
def cut(value, arg):
    return str(value).replace(arg, '')