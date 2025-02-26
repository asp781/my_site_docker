from django.shortcuts import render
from django.db.models import Sum
from .models import *

def index(request,slug):
    estimate = Estimate.objects.get(slug=slug)
    purchased = Purchased.objects.filter(estimate=estimate)
    completed = Completed.objects.filter(estimate=estimate)
    paid = Paid.objects.filter(estimate=estimate)

    purchased_sum = round(sum(float(row.total_price) for row in purchased), 2)
    completed_sum = round(sum(float(row.total_price) for row in completed if row.total_price != ''), 2)
    paid_sum = round(sum(float(row.total_price) for row in paid), 2)
    balance = round((purchased_sum + completed_sum + paid_sum), 2)

    return render(request, "secret2/index.html", {
                'purchased': purchased,
                'completed': completed,
                'paid': paid,
                'purchased_sum': purchased_sum,
                'completed_sum': completed_sum,
                'paid_sum': paid_sum,
                'balance': balance,
                })
