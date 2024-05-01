from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer

from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import api_view, permission_classes

# Create your views here.

def index(request):
    return render(request, 'restaurant/index.html')

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

#@api_view
#@permission_classes([IsAuthenticated])    
    

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    