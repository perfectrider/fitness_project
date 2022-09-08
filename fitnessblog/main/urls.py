from django.contrib.auth import login
from django.urls import path
from . import views
from .views import LoginUser, logout_user
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.MainPage.as_view(), name='Главная'),
    path('about', views.AboutPage.as_view(), name='Обо мне'),
    path('addarticle', views.AddArticle.as_view(), name='Добавить статью'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('<slug:slug>', views.ArticlesDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/update/', views.ArticlesUpdate.as_view(), name='update_article'),
    path('<slug:slug>/delete/', views.ArticlesDelete.as_view(), name='delete_article'),
]
