from django.urls import path
from clients import views
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('token_auth/', authtoken_views.obtain_auth_token)
]