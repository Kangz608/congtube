from django import template

register = template.Library()


@register.filter(name='greens')
def greens(number):
    return range(round(number))


@register.filter(name='greys')
def greys(number):
    return range(5-round(number))
