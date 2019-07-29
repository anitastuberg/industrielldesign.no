from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import JsonResponse
import datetime


from .forms import ArticleForm
from .models import Article


def wiki(request):
    articles = Article.objects.all()[:1000]

    responseData = {}

    query = request.GET.get('q')
    if query:
        result_articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(introduction__icontains=query) |
            Q(body_text__icontains=query)
        ).distinct()

        for i in range(len(result_articles)):
            responseData['article%s' % i] = {
                'title': result_articles[i].title,
                'introduction': result_articles[i].introduction,
                'body_text': result_articles[i].body_text,
                'slug': result_articles[i].slug
            }

        return JsonResponse(responseData)

    context = {
        'articles': articles
    }
    return render(request, 'wiki/wiki.html', context)


def new_article(request):
    # Calls 403 - permission denied if not logged in
    if request.user.is_authenticated:

        form = ArticleForm(request.POST or None)

        if request.method == 'POST':

            if form.is_valid():
                now = datetime.datetime.now()
                new_article = form.save(commit=False)
                new_article.editable = True
                new_article.updated = now
                new_article.save()
                now = datetime.datetime.now()
                subject = 'WIKI NY: "%s" har blitt opprettet' % (
                    new_article.title)
                message = 'Opprettet: %s av %s %s\nindustrielldesign.no/wiki/%s' % (now.strftime(
                    "%d.%m.%y %H:%M"), request.user.first_name, request.user.last_name, new_article.slug)
                wiki_email(subject, message)
                return redirect('article', article_slug=new_article.slug)

        context = {
            'form': form
        }

        return render(request, 'wiki/new-article.html', context)

    # If not logged in raise 403-page
    else:
        raise PermissionDenied


def wiki_email(subject, message):
    send_mail(
        subject,  # Subject
        message,  # Message
        settings.EMAIL_HOST_USER,  # From email
        [settings.EMAIL_HOST_USER],  # To email
        fail_silently=False,
    )


def edit_article(request, article_slug):

    # Retrieve the matching article model
    article = Article.objects.get(slug=article_slug)

    # Check if user is logged in and article can be edited
    # Staff can edit all articles
    if (request.user.is_authenticated and article.editable) or request.user.is_staff:

        # Prepopulates the form with the articles data
        form = ArticleForm(instance=article)

        if request.method == 'POST':
            # Get the new data from the sent form
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                now = datetime.datetime.now()
                subject = 'WIKI: "%s" har blitt oppdatert' % (article.title)
                message = "Oppdatert: %s av %s %s\nindustrielldesign.no/wiki/%s" % (now.strftime(
                    "%d.%m.%y %H:%M"), request.user.first_name, request.user.last_name, article.slug)
                wiki_email(subject, message)  # Sends email to "webredaktør"
                updated_article = form.save(commit=False)
                updated_article.updated = now
                updated_article.save()
                return redirect('article', article_slug=article.slug)
        # If GET request or not valid data
        return render(request, 'wiki/new-article.html', {'form': form})

    # If user is not signed in. Redirect to 403-page
    else:
        raise PermissionDenied


def article(request, article_slug):
    article = Article.objects.get(slug=article_slug)

    article.visits += 1
    article.save()

    context = {
        'article': article
    }
    return render(request, 'wiki/article.html', context)
