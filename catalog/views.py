from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_avialable=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    count_genres=Genre.objects.filter(name__iregex=r'\b' + 'фантастика' + r'\b').count()
    count_books=Book.objects.filter(title__iregex=r'\b' + 'window' + r'\b').count()


    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_avialable, 'num_authors':num_authors,
                 'count_genres':count_genres, 'count_book':count_books},
    )

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book