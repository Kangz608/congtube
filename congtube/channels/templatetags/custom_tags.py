from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def deadline(value, arg):
    deadline = arg + timedelta(days=7)

    return deadline