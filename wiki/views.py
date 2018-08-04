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

        form = ArticleForm(request.POST or None)

        if request.method == 'POST':

            if form.is_valid():

                new_article = form.save(commit=False)
                new_article.save()
                return redirect('article', article_slug=new_article.slug)


        context = {
            'form': form
        }

        return render(request, 'wiki/new-article.html', context)
    
    # If not logged in raise 403-page    
    else:
        raise PermissionDenied

def edit_article(request, article_slug):
    # Check if user is logged in
    if request.user.is_authenticated:

        # Retriece the matching article model
        article = Article.objects.get(slug=article_slug)
        # Prepopulates the form with the articles data
        form = ArticleForm(instance=article)

        if request.method == 'POST':
            # Get the new data from the sent form
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article', article_slug=article.slug)
        # If GET request or not valid data
        return render(request, 'wiki/new-article.html', {'form' : form})


    # If user is not signed in. Redirect to 403-page
    else:
        raise PermissionDenied



def article(request, article_slug):
    print(article_slug)
    article_model = Article.objects.get(slug=article_slug)

    context = {
        'article' : article_model
    }
    return render(request, 'wiki/article.html', context)