from django.forms import ModelForm
from django import forms
from .models import Article

class AddArticleForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Article
        exclude = ['title']