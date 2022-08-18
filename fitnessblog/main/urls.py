from django.urls import path
from . import views
# from .views import article_show

urlpatterns = [
    path('', views.index, name='Главная'),
    path('about/', views.about, name='О нас'),
    path('article/<int:article_id>/', views.ArticlesDetailView.as_view(), name='article_detail'),
]
