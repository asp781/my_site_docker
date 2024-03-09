from django.urls import path, re_path
# from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', all_service, name='price'),
    path('category/<slug:cat_slug>/', service_by_category, name='category'),
    path('post/<int:post_id>/', service_detail, name='post'),
]
