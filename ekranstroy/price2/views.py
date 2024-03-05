from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import *



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('service')).order_by('id')
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


class PriceHome(DataMixin, ListView):
    model = Service
    template_name = 'price/index.html'
    context_object_name = 'services'
    paginate_by = 60

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Все категории услуг")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Service.objects.filter(is_published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Service
    template_name = 'price/service.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['service'])
        return dict(list(context.items()) + list(c_def.items()))


class ServiceCategory(DataMixin, ListView):
    model = Service
    template_name = 'price/index.html'
    context_object_name = 'services'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
