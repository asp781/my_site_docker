from django.db import models
from django.utils.text import slugify

class Estimate(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Purchased(models.Model):
    date = models.CharField(max_length=255, null=True, blank=True) # Дата
    title = models.CharField(max_length=255, null=True, blank=True) # Название
    amount = models.CharField(max_length=255, null=True, blank=True) # Сумма
    unit = models.CharField(max_length=255, null=True, blank=True) # Единица измерения
    price = models.CharField(max_length=255, null=True, blank=True) # Цена
    total_price = models.CharField(max_length=255, null=True, blank=True) # Общая стоимость
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE) # Смета

class Completed(models.Model):
    date = models.CharField(max_length=255, null=True, blank=True) # Дата
    title = models.CharField(max_length=255, null=True, blank=True) # Название
    amount = models.CharField(max_length=255, null=True, blank=True) # Сумма
    unit = models.CharField(max_length=255, null=True, blank=True) # Единица измерения
    price = models.CharField(max_length=255, null=True, blank=True) # Цена
    total_price = models.CharField(max_length=255, null=True, blank=True) # Общая стоимость
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE) # Смета

class Paid(models.Model):
    date = models.CharField(max_length=255, null=True, blank=True) # Дата
    title = models.CharField(max_length=255, null=True, blank=True) # Название
    amount = models.CharField(max_length=255, null=True, blank=True) # Сумма
    unit = models.CharField(max_length=255, null=True, blank=True) # Единица измерения
    price = models.CharField(max_length=255, null=True, blank=True) # Цена
    total_price = models.CharField(max_length=255, null=True, blank=True) # Общая стоимость
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE) # Смета
