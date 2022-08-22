from django.db import models
from django.db.models import PROTECT


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    # добавил ключ для связи с таблицей категорий
    category = models.ForeignKey('Category', on_delete=PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    '''Модель, определяющая название категории статей,
    по которым будут группироваться статьи, с присвоенными
    им категориям'''
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
