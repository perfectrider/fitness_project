from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='Главная'),
    path('about', views.AboutPage.as_view(), name='Обо мне'),
    path('addarticle', views.addarticle, name='Добавить статью'),
    path('<slug:slug>', views.ArticlesDetailView.as_view(), name='article_detail'),
]
