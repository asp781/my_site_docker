from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect


def web8000_ekranstroy_middleware(get_response):
    def middleware(request):
        request.META['HTTP_HOST'] = 'ekranstroy.ru'
        request.META['wsgi.url_scheme'] = 'https'
        host = request.get_host()
        response = get_response(request)
        return response
    return middleware

# 'account.middleware.web8000_ekranstroy_middleware',
