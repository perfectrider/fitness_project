from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, TemplateView

from main.forms import *
from main.models import *

class MainPage(ListView):
    '''Класс отображения главной страницы'''

    model = Article
    template_name = 'main/index.html'
    context_object_name = 'articles'
    extra_context = {'title': 'Фитнес блог - главная страница'}

    def get_queryset(self):
        # Функция отображения только опубликованных статей
        return Article.objects.filter(is_published=True)

# def index(request):
    # Функция отображения главной страницы (старый вариант)
#     articles = Article.objects.order_by('-time_create')
#     return render(request, 'main/index.html',
#                   {'articles': articles,
#                    'title': 'Фитнес блог'})

class AboutPage(TemplateView):
    '''Класс отображения страницы обо мне'''

    template_name = 'main/about.html'
    context_object_name = 'Обо мне'
    extra_context = {'title': 'Эта страница обо мне'}

# def about(request):
    # Фукнция отображения страницы обо мне (старый вариант
    # return render(request, 'main/about.html',
    #               {'title': 'Обо мне'})


def addarticle(request):
    # Функция добавления статьи через форму ввода

    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Главная')
    else:
        form = AddArticleForm()
    return render(request, 'main/addarticle.html',
            {'form': form,
             'title': 'Добавить статью'})


class ArticlesDetailView(DetailView):
    '''Отдельное окно для полного просмотра статьи'''

    model = Article
    template_name = 'main/article.html'
    context_object_name = 'article'
    title = Article.title


def pageNotFound(request, exception):
    # Обработка исключения 404
    return HttpResponseNotFound('Такой страницы не существует!')
