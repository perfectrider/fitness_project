from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from main.forms import *
from main.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPage(ListView):
    '''Класс отображения главной страницы'''

    paginate_by = 4
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


class AddArticle(LoginRequiredMixin, CreateView):
    '''Класс добавления статьи через форму'''

    form_class = AddArticleForm
    template_name = 'main/addarticle.html'
    login_url = 'admin/'
    extra_context = {'title': 'Добавить статью'}


# def addarticle(request):
#     # Старый вариант Функции добавления статьи через форму ввода
#
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Главная')
#     else:
#         form = AddArticleForm()
#     return render(request, 'main/addarticle.html',
#                   {'form': form,
#                    'title': 'Добавить статью'})


class ArticlesDetailView(DetailView):
    '''Отдельное окно для полного просмотра статьи'''

    model = Article
    template_name = 'main/article.html'
    context_object_name = 'article'
    title = Article.title


class RegisterUser(CreateView):
    '''Регистрация пользователя на сайте'''

    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User


def pageNotFound(request, exception):
    # Обработка исключения 404
    return HttpResponseNotFound('Такой страницы не существует!')
