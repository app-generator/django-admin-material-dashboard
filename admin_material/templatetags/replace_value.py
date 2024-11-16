from django import template

register = template.Library()


@register.filter(name="replace_value")
def replace_value(value, arg):
  return value.replace(arg, " ").title()