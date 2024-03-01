from django.urls import path
from .views import create_short_url, redirect_to_original, hello_world

app_name = 'shortSnip'

urlpatterns = [
    path('', hello_world, name='home'),
    path('create_short_url/', create_short_url, name='create_short_url'),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
]
