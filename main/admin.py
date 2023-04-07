from django.contrib import admin
from .models import *

class MenuLevel01Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(MenuLevel01, MenuLevel01Admin)

class MenuLevel02Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(MenuLevel02, MenuLevel02Admin)

class MenuLevel03Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(MenuLevel03, MenuLevel03Admin)
