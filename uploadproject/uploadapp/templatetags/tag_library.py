from django import template

register = template.Library()

@register.filter(name='int')
def to_int(value):
    return int(value)

@register.filter(name='str')
def to_string(value):
    return str(value)