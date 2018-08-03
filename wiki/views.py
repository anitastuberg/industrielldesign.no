from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.exceptions import PermissionDenied, ValidationError

from .forms import ArticleForm
from .models import Article

def wiki(request):
    context = {
        'article' : Article.objects.all()
    }
    return render(request, 'wiki/wiki.html', context)



def new_article(request):
    # Calls 403 - permission denied if not logged in
    if request.user.is_authenticated:

        form = ArticleForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():

            new_article = form.save(commit=False)
            image = form.cleaned_data['image']
            new_article.save()
            return redirect('article', article=new_article.slug)

        context = {
            'form': form
        }

        return render(request, 'wiki/new-article.html', context)
    else:
        raise PermissionDenied



def article(request, article):
    print(article)
    article_model = Article.objects.get(slug=article)

    context = {
        'article' : article_model
    }
    return render(request, 'wiki/article.html', context)