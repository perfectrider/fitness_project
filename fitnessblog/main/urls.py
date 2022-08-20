from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Главная'),
    path('about', views.about, name='О нас'),
    path('<int:pk>', views.ArticlesDetailView.as_view(), name='article_detail'),
]
