from django.contrib.auth import login
from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.MainPage.as_view(), name='Главная'),
    path('about', views.AboutPage.as_view(), name='Обо мне'),
    path('addarticle', views.AddArticle.as_view(), name='Добавить статью'),
    path('login', login, name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('<slug:slug>', views.ArticlesDetailView.as_view(), name='article_detail'),
]
