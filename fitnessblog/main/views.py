from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from main.forms import *
from main.models import *


def index(request):
    articles = Article.objects.order_by('-time_create')
    return render(request, 'main/index.html',
                  {'articles': articles,
                   'title': 'Фитнес блог'})

def about(request):
    return render(request, 'main/about.html',
                  {'title': 'Обо мне'})

def addarticle(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            try:
                Article.objects.create(**form.cleaned_data)
                return redirect('Главная')
            except:
                form.add_error(None, 'Пост не добавлен!')
    else:
        form = AddArticleForm()
    return render(request, 'main/addarticle.html',
            {'form': form,
             'title': 'Добавить статью'})

class ArticlesDetailView(DetailView):
    # Отдельное окно для полного просмотра статьи
    model = Article
    template_name = 'main/article.html'
    context_object_name = 'article'
    title = Article.title

def pageNotFound(request, exception):
    return HttpResponseNotFound('Такой страницы не существует!')
