# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='split_comma')
def split_comma(value):
    return value.split(', ')
