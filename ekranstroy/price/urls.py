from django.urls import path, re_path
# from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', PriceHome.as_view(), name='price'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ServiceCategory.as_view(), name='category'),
]
