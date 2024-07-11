#define URL route for index() view
from django.urls import path
from . import views
from .views import MenuItemView,SingleMenuItemView


urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/',MenuItemView.as_view(),name='menu-items' ),
    path('menu-items/<int:pk>/',SingleMenuItemView.as_view(),name='single-menu-items' ),
    
]
