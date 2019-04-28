from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import Profile
from books.models import Book
from courses.models import Course


def books(request):
    context = {
        'books': Book.objects.all(),
    }
    if request.method == 'GET':
        return render(request, 'books/books.html', context)
    else:  # POST
        # Filter books
        books = Book.objects.filter(title=request.POST.get("title"))
        return JsonResponse({
            'books': books
        })


def create_book(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'books/create-book.html', context)
    else:  # POST
        title = request.POST.get('title')
        course_code = request.POST.get('course').split(" ")[-1]
        print(course_code)
        user = Profile.objects.get(pk=request.user.pk)
        course = Course.objects.get(course_code=course_code)
        price = request.POST.get('price')
        image = request.FILES.get('image')
        print(image)
        Book.objects.create(title=title,
                            seller=user,
                            course=course,
                            image=image,
                            price=price)
        return redirect('books')