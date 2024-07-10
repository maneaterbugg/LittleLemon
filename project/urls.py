#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter   
from myapp.views import BookingViewSet

router= DefaultRouter()
router.register(r'bookings', BookingViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('restaurant/', include('myapp.urls')),
   path('restaurant/booking/', include(router.urls)),
]
