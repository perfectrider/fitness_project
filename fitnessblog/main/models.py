from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title