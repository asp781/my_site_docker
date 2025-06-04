from rest_framework import generics
from rest_framework.permissions import AllowAny
from secret2.models import Estimate, Purchased, Completed, Paid
from .serializers import EstimateSerializer, PurchasedSerializer, CompletedSerializer, PaidSerializer

class EstimateListCreate(generics.ListCreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [AllowAny]

class EstimateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [AllowAny]

class PurchasedListCreate(generics.ListCreateAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer
    permission_classes = [AllowAny]

class PurchasedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer
    permission_classes = [AllowAny]

class CompletedListCreate(generics.ListCreateAPIView):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer
    permission_classes = [AllowAny]

class CompletedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer
    permission_classes = [AllowAny]

class PaidListCreate(generics.ListCreateAPIView):
    queryset = Paid.objects.all()
    serializer_class = PaidSerializer
    permission_classes = [AllowAny]

class PaidRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paid.objects.all()
    serializer_class = PaidSerializer
    permission_classes = [AllowAny]

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
