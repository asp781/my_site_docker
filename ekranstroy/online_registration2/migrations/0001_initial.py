# Generated by Django 4.2.9 on 2024-02-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('order_phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('order_day', models.DateField()),
                ('order_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
