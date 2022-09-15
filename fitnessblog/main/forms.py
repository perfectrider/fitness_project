from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *


class AddArticleForm(forms.ModelForm):
    '''Новый вариант класса, наследующий поля модели Article'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'is_published', 'image', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 120, 'rows': 10}),
        }


class RegisterUserForm(UserCreationForm):
    '''Регистрация пользователя'''

    captcha = CaptchaField()

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'name@example.com'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Введите пароль еще раз',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    '''Авторизация пользователя'''

    captcha = CaptchaField()

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    '''Создание комментирия под постом'''

    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': '2',
        'class': 'form-control',
        'placeholder': 'Введите комментарий сюда'
    }))

    class Meta:
        model = Comments
        fields = ('comment',)



