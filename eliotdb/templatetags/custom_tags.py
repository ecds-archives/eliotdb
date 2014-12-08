from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
def strip_eliot(self):
    return self.lstrip('eliot_')
