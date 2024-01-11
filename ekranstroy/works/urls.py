from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('o_nas/', o_nas, name='o_nas'),
    path('uslugi/', uslugi, name='uslugi'),
    path('price/', price, name='price'),
    path('technologi/', technologi, name='technologi'),
    path('nasi_raboti/', nasi_raboti, name='nasi_raboti'),
    path('contacts/', contacts, name='contacts'),
    path('gostinica/', gostinica, name='gostinica'),
    path('dom/', dom, name='dom'),
    path('otdelka/', otdelka, name='otdelka'),
    path('avtoservis/', avtoservis, name='avtoservis'),
    path('vibor_uchastka/', vibor_uchastka, name='vibor_uchastka'),
    path('raschet/', raschet, name='raschet'),
    path('analiz_grunta/', analiz_grunta, name='analiz_grunta'),
    path('penoblok/', penoblok, name='penoblok'),
    path('etapy/', etapy, name='etapy'),
    path('etapy_remonta/', etapy_remonta, name='etapy_remonta'),
    path('mailto/', mailto, name='mailto'),
]
