from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
# Create your views here.

def index(request):
    return render(request, 'restaurant/index.html')

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer