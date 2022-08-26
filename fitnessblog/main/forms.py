from django import forms
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
