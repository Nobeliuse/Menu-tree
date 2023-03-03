from .models import Menu

def get_children(menu_item):
    children = Menu.objects.filter(parent=menu_item).order_by('name')
    if children:
        return [{'item': c, 'children': get_children(c)} for c in children]
    return []