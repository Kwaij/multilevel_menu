from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'main/home.html', {'title': 'Главная'})

def menu_01(request, slug_01):
    menu_02 = MenuLevel02.objects.filter(cat__slug=slug_01).select_related('cat')
    title = MenuLevel01.objects.get(slug=slug_01)
    return render(request, 'main/menu_detail.html', {'menu_02': menu_02,'title': title})

def menu_02(request, slug_01, slug_02):
    menu_03 = MenuLevel03.objects.filter(cat__slug=slug_02).select_related('cat__cat')
    my_objects = MenuLevel02.objects.get(slug=slug_02)
    title = my_objects
    parent = my_objects.cat
    return render(request, 'main/menu_detail.html', {'menu_03': menu_03,'title': title,'parent': parent})

def menu_03(request, slug_01, slug_02, slug_03):
    title = MenuLevel03.objects.get(slug=slug_03)
    my_objects = MenuLevel02.objects.get(slug=slug_02)
    parent = my_objects
    parent_parent = my_objects.cat
    return render(request, 'main/menu_detail.html', {'title': title,'parent': parent,'parent_parent': parent_parent})