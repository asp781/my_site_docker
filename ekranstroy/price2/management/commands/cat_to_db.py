from django.core.management.base import BaseCommand
from pathlib import Path
from price.models import Category

dir = Path(__file__).parent

class Command(BaseCommand):

    filename = 'url.csv'

    def handle(self, *args, **options):
        with open(dir / self.filename, encoding='utf-8') as file:

            while True:
                line = file.readline()
                row = line.split(';')
                if not line: break

                Category.objects.get_or_create(
                    name=row[0],
                    slug=row[1].replace('https://tula.leroymerlin.ru/uslugi/', '').replace('/\n', '')
                )
            self.stdout.write(f'Данные из {self.filename} загружены')


# python manage.py cat_to_db
# ﻿Установка входной двери
