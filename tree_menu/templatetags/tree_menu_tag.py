from django import template
from tree_menu.models import Menu
from tree_menu.utils import get_children

register = template.Library()


@register.inclusion_tag('tree_menu/include/list_menu.html')
def draw_menu(selected):
    root_menu_items = Menu.objects.filter(parent=None).order_by('name')
    menu_items = [{'item': item, 'children': get_children(item)} for item in root_menu_items]
    return {'menu_items': menu_items, 'selected': selected}
