from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chatapp-home'),
    path('<str:room_name>/', views.room, name='room'),
    path('about/', views.about, name='chatapp-about'),
]
