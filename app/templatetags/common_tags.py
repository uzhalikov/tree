from django import template
from app.models import *

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }