from django.urls import path
from clients import views

urlpatterns = [
    path('trips/', views.trip_list)
]