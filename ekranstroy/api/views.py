from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from price.models import Category
from online_registration.models import Order
from .serializers import *

@api_view(['GET'])
def cat_list(request):
    # if request.method == 'POST':
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Category.objects.all()[:10]
    serializer = CategorySerializer(cats, many=True)
    response = Response(serializer.data)
    response['Access-Control-Allow-Origin'] = '*'
    return response


@api_view(['GET'])
def order_list(request):
    cats = Order.objects.all()
    serializer = OrderSerializer(cats, many=True)
    return Response(serializer.data)
