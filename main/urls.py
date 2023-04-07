from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<slug:slug_01>/', views.menu_01, name='menu_01'),
    path('menu/<slug:slug_01>/<slug:slug_02>/', views.menu_02, name='menu_02'),
    path('menu/<slug:slug_01>/<slug:slug_02>/<slug:slug_03>/', views.menu_03, name='menu_03'),
] 