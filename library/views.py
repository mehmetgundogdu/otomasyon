from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render

from .models import Author, Book, Publisher


def index(request):
    return render(request, 'library/index.html')


def about(request):
    return render(request, 'library/about.html', {})


def contact(request):
    return render(request, 'library/contact.html', {})


def books(request):
    all_author = Author.objects.all()
    return render(request, 'library/books.html', {'all_author': all_author})


def all_books(request):
    books_all = Book.objects.all()
    return render(request, 'library/all_books.html', {'books_all': books_all})


def publishers(request):
    publisher_all = Publisher.objects.all()
    return render(request, 'library/publishers.html', {'publisher_all': publisher_all})


def detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Boyle bir yazar yok")
    return render(request, 'library/detail.html', {'author': author})


def kitapdetayi(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Boyle bir kitap yok")
    return render(request, 'library/kitapdetayi.html', {'book': book})


def publishersdetail(request, publisher_id):
    try:
        publisher = Publisher.objects.get(pk=publisher_id)
    except Publisher.DoesNotExist:
        raise Http404("Boyle bir yayinevi yok")
    return render(request, 'library/publishersdetail.html', {'publisher': publisher})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                boks = Book.objects.filter(lendby=request.user)
                return render(request, 'library/login_user.html', {'boks': boks})
            else:
                return render(request, 'library/login.html', {'error_message': 'Hesap devre disi'})
        else:
            return render(request, 'library/login.html', {'error_message': 'Yanlış bilgiler'})
    return render(request, 'library/login.html')