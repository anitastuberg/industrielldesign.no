import simplejson
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from tips.models import Tip, Tag


def tips(request):
    filtered_tips = Tip.objects.all()
    context = {
        'tips': list(filtered_tips.values('title', 'slug')),
        'tags': Tag.objects.all,
        'tags_hack': simplejson.dumps(list(Tag.objects.filter(tip__in=filtered_tips).values('name')))
    }
    for i in range(0, len(context['tips'])):
        context['tips'][i]['tags'] = list(filtered_tips[i].tags.values('name'))

    if request.method == 'GET':
        return render(request, 'tips/tips.html', context)
    else:
        tags = request.POST.getlist('tags[]')
        filtered_tips = Tip.objects.filter(tags__name__in=tags)
        response = {
            'tips': list(filtered_tips.values('title', 'slug'))
        }
        for i in range(0, len(response['tips'])):
            response['tips'][i]['tags'] = list(filtered_tips[i].tags.values('name'))
        return JsonResponse(response)


def tip_page(request, tip_slug):
    context = {
        'tip': Tip.objects.get(slug=tip_slug)
    }
    return render(request, 'tips/tip-page.html', context)


def new_tip(request):
    if request.method == 'GET':
        return render(request, 'tips/new-tip.html', {})
    else:  # Post
        html = request.POST.get('html')
        title = request.POST.get('title')
        if html or title:
            Tip.objects.create(title=title, html=html)
            return HttpResponse('success')
        else:
            return HttpResponse('error')


def edit_tip(request, tip_slug):
    current_tips = Tip.objects.get(slug=tip_slug)
    context = {
        'edit_text': current_tips.html
    }
    if request.method == 'GET':
        return render(request, 'tips/new-tip.html', context)
    else:
        title = request.POST.get('title')
        html = request.POST.get('html')
        if html or title:
            current_tips.title = title
            current_tips.html = html
            current_tips.save()
            return HttpResponse('success')
        else:
            return HttpResponse('error')