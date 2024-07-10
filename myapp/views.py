from rest_framework import generics,viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSeralizer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSeralizer
   permission_classes = [IsAuthenticated]

def index(request):
 return render(request, 'index.html', {})    