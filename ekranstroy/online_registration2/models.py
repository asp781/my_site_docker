from django.db import models



class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_day = models.DateField()
    order_time = models.TimeField()


    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
