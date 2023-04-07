from django import template
from main.models import *

register = template.Library()

@register.inclusion_tag('main/menu.html')
def show_menu():
    menu_level_01 = MenuLevel01.objects.all()
    menu_level_02 = MenuLevel02.objects.all().select_related('cat')
    menu_level_03 = MenuLevel03.objects.all().select_related('cat__cat')
    return {'menu_01': menu_level_01,'menu_02': menu_level_02,'menu_03': menu_level_03,}
