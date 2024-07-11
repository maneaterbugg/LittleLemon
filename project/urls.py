#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter   
from myapp.views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router= DefaultRouter()
router.register(r'bookings', BookingViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('restaurant/', include('myapp.urls')),
   path('   ', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
   path('api-token-auth/', obtain_auth_token),
]
