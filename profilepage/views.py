from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from authentication.forms import RegisterForm
from authentication.models import Profile
from books.models import Book
from leonardo.models import Komite


def my_profile(request):
    try:
        user = Profile.objects.get(pk=request.user.pk)
    except Profile.DoesNotExist:
        return redirect('login')
    form = RegisterForm(instance=user)
    my_books = Book.objects.filter(
        seller=Profile.objects.get(pk=request.user.pk))
    context = {
        'user': user,
        'form': form,
        'my_books': my_books
    }

    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'profilepage/profilepage.html', context)

    else:
        form = RegisterForm(request.POST, instance=user)
        komite = form['komite'].value()
        allergies = form['allergies'].value()
        graduation_year = form['graduation_year'].value()
        print('Komite:', komite)
        if allergies:
            user.allergies = allergies
        if komite:
            user.komite = Komite.objects.get(pk=komite)
        else:
            user.komite = None
        if graduation_year:
            user.graduation_year = graduation_year
        user.save()
        if request.POST.get('new-password'):
            password = request.POST['new-password']
            user.set_password(password)
            user.save()
            login(request, authenticate(
                request, email=user.email, password=user.password))

        context['form'] = RegisterForm(instance=user)
        return render(request, 'profilepage/profilepage.html', context)


def delete_book(request):
    book_pk = request.POST.get('book_pk')
    Book.objects.filter(pk=book_pk).delete()
    return HttpResponse('deleted')
