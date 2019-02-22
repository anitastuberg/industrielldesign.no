from django.shortcuts import render, redirect

from authentication.models import Profile
from courses.forms import CreateCourseForm, CreateCourseReviewForm
from courses.models import Course, CourseReview


def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/courses.html', context)


def create_course(request):
    form = CreateCourseForm()
    if request.method == 'GET':
        return render(request, 'courses/create-course.html', {'form': form})

    else: #POST
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            course_code = form.cleaned_data['course_code']
            Course.objects.create(name=name, course_code=course_code)
            return redirect('courses')
        else:
            return render(request, 'courses/create-course.html', {'form': form})


def course_detail(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    form = CreateCourseReviewForm()
    context = {
        'course': course,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'courses/course-detail.html', context)
    else: #POST
        form = CreateCourseReviewForm(request.POST)
        user = Profile.objects.get(pk=request.user.pk)
        if form.is_valid() and request.user.is_authenticated:
            text = form.cleaned_data['text']
            course_review = CourseReview.objects.create(text=text, author=user)
            course.reviews.add(course_review)
        return render(request, 'courses/course-detail.html', context)