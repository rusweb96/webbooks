from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()
    # число посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'text_head': text_head,
        'books': books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'authors': authors,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3
    template_name = 'catalog/book_list.html'


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    paginate_by = 4
    template_name = 'catalog/author_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author_detail.html'
