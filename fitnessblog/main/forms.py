from django import forms
from .models import *

class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=250, label='Название статьи')
    slug = forms.SlugField(max_length=25, label='URL адрес')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст статьи')
    is_published = forms.BooleanField(initial=True,
                                      required=False,
                                      label='Опубликовать',
                                      widget=forms.CheckboxInput(attrs={'class': "form-check-label"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label='Категория не выбрана',
                                      label='Категория')

