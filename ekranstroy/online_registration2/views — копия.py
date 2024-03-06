from django.shortcuts import render
from .models import Order
from datetime import datetime



def first_page(request):
    all_time = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")

    if request.GET.get('date') is None:
        dict_obj = {'min_day_value': min_day_value,
                    'all_time': all_time,
                    'step_1': True,
                    'step': 'Шаг 1',}
        return render(request, 'online_registration/index.html', dict_obj)
    else:
        appointments = Order.objects.filter(order_day=request.GET.get('date')).all()
        for obj in appointments:
            all_time.remove(obj.order_time.strftime("%H:%M"))
        dict_obj = {'min_day_value': min_day_value,
                    'all_time': all_time,
                    'step_1': False,
                    'step_2': True,
                    'step': 'Шаг 2',
                    'choised_day': request.GET.get('date')}
        return render(request, 'online_registration/index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        day = request.POST['date']
        time = request.POST['time']
        element = Order(order_name=name, order_phone=phone, order_day=day, order_time=time )
        element.save()
        return render(request, 'online_registration/thanks.html', {'name': name})
    else:
        return render(request, 'online_registration/thanks.html')


# https://www.youtube.com/watch?v=cGW9VIOe1Ng&list=WL&index=29&t=44s
