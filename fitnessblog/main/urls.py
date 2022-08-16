from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Главная'),
    path('about/', about, name='О нас'),
    path('article/<int:article_id>/', article_show),
]
