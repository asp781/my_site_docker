import os
import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand
from secret2.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):

        # file = "D:\Заказы\REV24.xlsx"
        file = os.path.join(os.path.dirname(__file__), 'Сметы.xlsx')
        sheet_name='Сур22-139'

        try:
            df = pd.read_excel(
                io=file,
                sheet_name=sheet_name,
                usecols=[0,1,2,3,4,5],
                header=None,
                dtype='str',
            )
        except ValueError:
            return print(f'Ошибка')

        # Преобразуем datafame в list до 'К оплате', убираем пустые строки
        data = []
        for row in range(len(df)):
            if str(list(df.iloc[row])) != '[nan, nan, nan, nan, nan, nan]':
                data.append((list(df.iloc[row])))
            if df.iloc[row, 1] == 'К оплате': break

        # Преобразуем даты, находим индексы, заменяем nan на '', убираем лишние знаки после запятой
        for row in range(len(data)):
            try:
                data[row][0] = datetime.strptime(data[row][0], '%Y-%m-%d %H:%M:%S').strftime("%d.%m.%Y")
            except: pass

            if data[row][1] == 'Закуплено': index_1 = row
            if data[row][1] == 'Выполнено': index_2 = row
            if data[row][1] == 'Оплачено': index_3 = row

            for cell in range(6):
                if str(data[row][cell]) == 'nan':
                    data[row][cell] = ''

            for col in [2, 4, 5]:
                if '.' in data[row][col]:
                    if len(data[row][col].split('.')[1]) > 2:
                        data[row][col] = data[row][col].split('.')[0] + '.' + data[row][col].split('.')[1][:2]


        # Разбиваем list на 3 части по найденым индексам
        data_purchased = data[: index_1]
        data_completed = data[index_1 + 1 : index_2]
        data_paid = data[index_2 + 1 : index_3]

        estimate, created = Estimate.objects.get_or_create(name=sheet_name)
        if created: print('Новая смета!')
        else: print('Смета уже существует!')

        Purchased.objects.filter(estimate=estimate).delete()
        for row in range(len(data_purchased)):
            Purchased.objects.create(
                date = data_purchased[row][0],
                title=data_purchased[row][1],
                amount=data_purchased[row][2],
                unit=data_purchased[row][3],
                price=data_purchased[row][4],
                total_price=data_purchased[row][5],
                estimate=estimate,
                )
        Completed.objects.filter(estimate=estimate).delete()
        for row in range(len(data_completed)):
            Completed.objects.create(
                date = data_completed[row][0],
                title=data_completed[row][1],
                amount=data_completed[row][2],
                unit=data_completed[row][3],
                price=data_completed[row][4],
                total_price=data_completed[row][5],
                estimate=estimate,
                )
        Paid.objects.filter(estimate=estimate).delete()
        for row in range(len(data_paid)):
            Paid.objects.create(
                date = data_paid[row][0],
                title=data_paid[row][1],
                amount=data_paid[row][2],
                unit=data_paid[row][3],
                price=data_paid[row][4],
                total_price=data_paid[row][5],
                estimate=estimate,
                )

# cd /d/Dev/my_site_docker&&venv&&cd ekranstroy/&&rs
# python manage.py load_est
#  test.xlsx Смета_1
