from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from authentication.models import Profile
from .forms import CreateCourseForm, CreateCourseReviewForm
from .models import Course, CourseReview, CourseLink


def courses(request):
    context = {
        'courses': Course.objects.filter(Q(reviews__isnull=False) | Q(display_without_reviews=True)).order_by('-reviews', 'name')
    }
    return render(request, 'courses/courses.html', context)


def create_course(request):
    form = CreateCourseForm()
    if request.method == 'GET':
        return render(request, 'courses/create-course.html', {'form': form})

    else:  # POST
        if request.POST.get('query'):  # ajax request
            query = request.POST.get('query').upper()
            course_suggestions = Course.objects.filter(Q(name__contains=query) | Q(course_code__contains=query)).values('name', 'course_code')
            return JsonResponse({'suggestions': list(course_suggestions)[:10]})
        else:
            form = CreateCourseForm(request.POST)
            if form.is_valid():
                course_code = form.cleaned_data['course_code']
                if Course.objects.filter(course_code=course_code).exists():
                    existing_course = Course.objects.get(course_code=course_code)
                    existing_course.display_without_reviews = True
                    existing_course.class_year = form.cleaned_data['class_year']
                    existing_course.save()
                    return redirect('courses')

            return render(request, 'courses/create-course.html', {'form': form})


def course_detail(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    form = CreateCourseReviewForm()
    context = {
        'course': course,
        'form': form,
        'links': CourseLink.objects.filter(course=course)
    }
    if request.method == 'GET':
        return render(request, 'courses/course-detail.html', context)
    else:  # POST
        if request.POST.get("text"):
            form = CreateCourseReviewForm(request.POST)
            user = Profile.objects.get(pk=request.user.pk)
            if form.is_valid() and request.user.is_authenticated:
                text = form.cleaned_data['text']
                course_review = CourseReview.objects.create(text=text, author=user)
                course.reviews.add(course_review)
            return render(request, 'courses/course-detail.html', context)
        else:
            title = request.POST.get('url_data[title]')
            description = request.POST.get('url_data[description]')
            image = request.POST.get('url_data[image]')
            url = request.POST.get('url_data[url]')
            CourseLink.objects.create(url_title=title,
                                             url_description=description,
                                             img_url=image,
                                             url=url,
                                             course=course)
            return HttpResponse("Success")
