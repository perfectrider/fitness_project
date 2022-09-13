from django.contrib.auth.models import User
from django.db import models
from django.db.models import PROTECT
from django.urls import reverse


class Article(models.Model):
    '''Модель, определяющая все параметры статьи.'''

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
        return reverse('article_detail', kwargs={'slug': self.slug})


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


class Comments(models.Model):
    '''Комментарии под постом.'''

    comment = models.TextField(blank=True, verbose_name='Введите текст комментария', )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан комментарий')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey(Article,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='comments_articles',
                                verbose_name='Статья')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['time_create']

    def __str__(self):
        return self.comment
