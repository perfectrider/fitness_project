from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Главная страница приложения')

def about(request):
    return HttpResponse('О нас.')

def article_show(requst, article_id):
    if requst.GET:
        print(requst.GET)
    return HttpResponse(f'Читать полностью...{article_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Такой страницы не существует!')
