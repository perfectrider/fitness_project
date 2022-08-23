from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from main.models import Article


def index(request):
    articles = Article.objects.order_by('-time_create')
    return render(request, 'main/index.html',
                  {'title': 'Фитнес блог', 'articles': articles})

def about(request):
    return render(request, 'main/about.html',
                  {'title': 'Обо мне'})

# def article_show(request, article_id):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'Читать полностью...{article_id}')

class ArticlesDetailView(DetailView):
    # Отдельное окно для полного просмотра статьи
    model = Article
    template_name = 'main/article.html'
    context_object_name = 'article'
    title = Article.title

    # def ArticlesDetailView(request, article_id):
    #     article = get_object_or_404(Article, pk=article_id)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Такой страницы не существует!')
