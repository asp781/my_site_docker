from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *



def all_service(request):
    """Отображение всех категорий и всех услуг."""
    template_name = 'price/index.html'
    cats = Category.objects.filter(is_published=True)
    cats_id = cats.values('id')
    services = Service.objects.filter(is_published=True, cat__in=cats_id)

    paginator = Paginator(services, 29)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Услуги',
        'cats': cats,
        'paginator': paginator,
        'page_obj': page_obj,
        }
    return render(request, template_name, context)


def service_by_category(request, cat_slug):
    """Отображение всех категорий и услуг из выбранной категории."""
    template_name = 'price/index.html'
    services = Service.objects.filter(cat__slug=cat_slug, is_published=True)
    cats = Category.objects.filter(is_published=True)

    paginator = Paginator(services, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Услуги',
        'cats': cats,
        'paginator': paginator,
        'page_obj': page_obj,
        }
    return render(request, template_name, context)


def service_detail(request, post_id):
    """Отображение детальной информации о выбранной услуге"""
    template_name = 'price/service.html'
    service = Service.objects.get(id=post_id)
    cats = Category.objects.all()
    context = {
        'title': 'Подробно',
        'service': service,
        'cats': cats,
        }
    return render(request, template_name, context)
