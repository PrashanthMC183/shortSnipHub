from django.urls import path
from .views import create_snippet, snippet_detail

app_name = 'snippet'

urlpatterns = [
    path('create_snippet/', create_snippet, name='create_snippet'),
    path('<int:pk>/', snippet_detail, name='snippet_detail'),
]