from django.db import models
from django.db.models import PROTECT
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Отредактировано')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # добавил ключ для связи с таблицей категорий
    category = models.ForeignKey('Category', on_delete=PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create']

    def get_absolute_url(self):
        return reverse('getlink:article_detail', kwargs={'slug': self.slug})

class Category(models.Model):
    '''Модель, определяющая название категории статей,
    по которым будут группироваться статьи, с присвоенными
    им категориям'''
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
