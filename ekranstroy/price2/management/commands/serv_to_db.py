from django.core.management.base import BaseCommand
from price.models import Service, Category

from .pars_html import func

class Command(BaseCommand):

    def handle(self, *args, **options):

        for n in range(1, 162):
            try:

                for i in func(n):

                    Service.objects.get_or_create(
                        type_service = i['type_service'],
                        title = i['title'],
                        price = i['price'],
                        unit = i['unit'],
                        content = i['content'],
                        hint = i['hint'],
                        cat_id = Category.objects.get(name=i['cat']).id,
                    )

                self.stdout.write(f'Данные из {n}.html загружены')

            except Exception as e:
                print(n, 'Неудача', e)

# python manage.py serv_to_db
