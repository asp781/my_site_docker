from django.contrib import admin

from .models import *

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    fields = ('type_service','title', 'price', 'unit', 'cat', 'content', 'hint', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('is_published',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
