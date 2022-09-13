from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

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


class AboutPage(TemplateView):
    '''Класс отображения страницы обо мне'''

    template_name = 'main/about.html'
    context_object_name = 'Обо мне'
    extra_context = {'title': 'Эта страница обо мне'}


class AddArticle(LoginRequiredMixin, CreateView):
    '''Класс добавления статьи через форму'''

    form_class = AddArticleForm
    template_name = 'main/addarticle.html'
    login_url = 'login'
    extra_context = {'title': 'Добавить статью'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ArticlesDetailView(FormMixin, DetailView):
    '''Отдельное окно для полного просмотра статьи'''

    model = Article
    template_name = 'main/article.html'
    context_object_name = 'article'
    title = Article.title
    form_class = CommentForm

    def comments(request):
        comments = Comments.objects.all()
        return render(request, 'main/article.html', {'comments': comments})


class ArticlesUpdate(UpdateView):
    '''Редактирование статьи'''

    model = Article
    template_name = 'main/updatearticle.html'
    success_url = reverse_lazy('Главная')
    fields = ['title', 'content', 'image', 'is_published']


class ArticlesDelete(DeleteView):
    '''Удаление статьи'''

    model = Article
    template_name = 'main/deletearticle.html'
    success_url = reverse_lazy('Главная')


class RegisterUser(CreateView):
    '''Регистрация пользователя на сайте'''

    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Главная')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('Главная')


def logout_user(request):
    logout(request)
    return redirect('login')


# class CommentForm(LoginRequiredMixin, CreateView):
#     '''Добавление комментария'''
#
#     form_class = CommentForm
#     template_name = 'main/article.html'
#     login_url = 'login'
#     fields = ['comment']
#
#
# class ShowComment(ListView):
#     '''Просмотр комментария'''
#
#     model = Comments
#     context_object_name = 'comments'
#     template_name = 'main/article.html'
#
#     def get_queryset(self):
#         return Comments.objects.filter(is_published=True)


def pageNotFound(request, exception):
    # Обработка исключения 404
    return HttpResponseNotFound('Такой страницы не существует!')
