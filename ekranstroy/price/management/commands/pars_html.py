from bs4 import BeautifulSoup
import json
from pprint import pprint
from copy import copy
from pathlib import Path


dir = Path(__file__).parent


def func(n):

    with open(dir / 'html' / f'{n}.html', 'r', encoding='utf-8') as f:
        text = f.read()


    bs = BeautifulSoup(text, 'html.parser')
    script = bs.find('script', id="init").string.split('"serviceCard":')[1].split('"servicesAttributes"')[0].strip().rstrip(',')
    script += '}'


    with open(dir / 'json' / f'{n}_1.json', 'w', encoding='utf-8') as f:
        f.write(script)


    with open(dir / 'json' / f'{n}_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)


    lst = []
    dt = {}
    cat_name = data["notRootCategoryOptions"]["categoryTitle"]

    # 'ОСНОВНОЙ СЕРВИС'
    for i in data['mainServices']:

        dt['type_service'] = i['serviceType']
        dt['title'] = i['name']
        dt['price'] = i['price']
        dt['unit'] = i['measurementUnit']['name']
        dt['content'] = ' '.join(i['descriptions'][0:])
        dt['hint'] = i['hint'] if not i['hint'] == None else ''
        dt['cat'] = cat_name

        lst.append(copy(dt))

    # 'ДОПОЛНИТЕЛЬНЫЙ СЕРВИС'
    if data['additionalServices']:
        for i in data['additionalServices'][0]['services']:
            dt['type_service'] = i['serviceType']
            dt['title'] = i['name']
            dt['price'] = i['price']
            dt['unit'] = i['measurementUnit']['name']
            dt['content'] = ' '.join(i['descriptions'][0:])
            dt['hint'] = i['hint'] if not i['hint'] == None else ''
            dt['cat'] = cat_name

            lst.append(copy(dt))

    # 'ЗАМЕРЫ'
    i = data['measureService']

    dt['type_service'] = i['serviceType']
    dt['title'] = i['name']
    dt['price'] = i['price']
    dt['unit'] = i['measurementUnit']['name']
    dt['content'] = ' '.join(i['descriptions'][0:])
    dt['hint'] = i['hint'] if not i['hint'] == None else ''
    dt['cat'] = cat_name

    lst.append(copy(dt))

    return lst

# python manage.py serv_to_db

if __name__ == '__main__':

    pprint(func(2), sort_dicts=False)
