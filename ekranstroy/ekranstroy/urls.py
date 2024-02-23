from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from ekranstroy import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('works.urls')),
    # path('blog/', include('blog.urls', namespace='blog')),
    path('account/', include('account.urls')),
    path('online_registration/', include('online_registration.urls', namespace='online_registration')),
    path('price/', include('price.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
