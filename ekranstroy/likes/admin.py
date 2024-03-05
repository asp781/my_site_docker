from django.contrib import admin

from .models import ServiceLikes

@admin.register(ServiceLikes)
class ServiceLikesAdmin(admin.ModelAdmin):
    autocomplete_fields = ('liked_by', 'blog_post')
    list_display = ('pk', 'liked_by', 'blog_post', 'like', 'created')
