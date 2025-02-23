from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from ekranstroy import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('works.urls')),
    path('', include('likes.urls', namespace='likes')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('online_registration/', include('online_registration.urls', namespace='online_registration')),
    path('price/', include('price.urls')),
    path('api/v1/', include('api.urls')),
    path('secret/', include('app4.urls', namespace='app4')),
    path('secret2/', include('secret2.urls', namespace='secret2')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
