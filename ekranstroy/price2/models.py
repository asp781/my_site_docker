from django.db import models
from django.urls import reverse

class Service(models.Model):

    CHOICES = (
        ('ADDITIONAL', 'Дополнительные работы'),
        ('MAIN', 'Основные работы'),
        ('MEASURE', 'Замеры'),
    )
    type_service = models.CharField(max_length=255, choices = CHOICES, verbose_name="Вид услуги")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=10)
    content = models.TextField(blank=True, verbose_name="Описание")
    hint = models.TextField(blank=True, verbose_name="Подсказка")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_slug': self.slug})
        return reverse('post', kwargs={'post_id': self.id})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_published = models.BooleanField(default=False, verbose_name="Публикация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
