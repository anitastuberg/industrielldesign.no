from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.defaultfilters import slugify

from .forms import ArticleForm
from .models import Article

def wiki(request):
    context = {
        'FYI_article' : Article.objects.filter(category="FYI"),
        'LOL_article' : Article.objects.filter(category="LOL")
    }
    return render(request, 'wiki/wiki.html', context)



def new_article(request):
    title = "Welcome"

    #add a form
    form = ArticleForm(request.POST or None)

    context = {
        "title": title,
        'form': form
    }

    if form.is_valid():

        instance = form.save(commit=False)

        instance.save()
        print(instance.slug)
        return redirect('article', article=instance.slug)

    return render(request, 'wiki/new-article.html', context)



def article(request, article):
    print(article)
    article_model = Article.objects.get(slug=article)

    context = {
        'article' : article_model
    }
    return render(request, 'wiki/article.html', context)