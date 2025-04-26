# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# from price.models import Category
# from online_registration.models import Order
# from .serializers import *

# @api_view(['GET'])
# def cat_list(request):
#     cats = Category.objects.all()[:10]
#     serializer = CategorySerializer(cats, many=True)
#     response = Response(serializer.data)
#     response['Access-Control-Allow-Origin'] = '*'
#     return response


# @api_view(['GET'])
# def order_list(request):
#     cats = Order.objects.all()
#     serializer = OrderSerializer(cats, many=True)
#     return Response(serializer.data)

from rest_framework import generics
from secret2.models import Estimate, Purchased, Completed, Paid
from .serializers import EstimateSerializer, PurchasedSerializer, CompletedSerializer, PaidSerializer

class EstimateListCreate(generics.ListCreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer

class EstimateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer

class PurchasedListCreate(generics.ListCreateAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer

class PurchasedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer

class CompletedListCreate(generics.ListCreateAPIView):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer

class CompletedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer

class PaidListCreate(generics.ListCreateAPIView):
    queryset = Paid.objects.all()
    serializer_class = PaidSerializer

class PaidRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paid.objects.all()
    serializer_class = PaidSerializer
