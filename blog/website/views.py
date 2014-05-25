from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import AddArticleForm
# Create your views here.

def home(request):
    articles = Article.objects.all()

    return render(request, "home.html", locals())

def contact_us(request):

    return render(request, "contact.html", locals())

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    comments = Comment.objects.filter(article=article)
    return render(request, "show_article.html", locals())

def add_article(request):
    data = request.POST if request.POST else None
    form = AddArticleForm(data)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "add_article.html", locals())
