from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'works/index.html')

def o_nas(request):
    return render(request, 'works/o_nas.html')

def uslugi(request):
    return render(request, 'works/uslugi.html')

def price(request):
    return render(request, 'works/price.html')

def technologi(request):
    return render(request, 'works/technologi.html')

def nasi_raboti(request):
    return render(request, 'works/nasi_raboti.html')

def contacts(request):
    return render(request, 'works/contacts.html')

def gostinica(request):
    return render(request, 'works/gostinica.html')

def dom(request):
    return render(request, 'works/dom.html')

def otdelka(request):
    return render(request, 'works/otdelka.html')

def avtoservis(request):
    return render(request, 'works/avtoservis.html')

def vibor_uchastka(request):
    return render(request, 'works/vibor_uchastka.html')

def raschet(request):
    return render(request, 'works/raschet.html')

def analiz_grunta(request):
    return render(request, 'works/analiz_grunta.html')

def penoblok(request):
    return render(request, 'works/penoblok.html')

def etapy(request):
    return render(request, 'works/etapy.html')

def etapy_remonta(request):
    return render(request, 'works/etapy_remonta.html')

def mailto(request):
    return render(request, 'works/mailto.html')
