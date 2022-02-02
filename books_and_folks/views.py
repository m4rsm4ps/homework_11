from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, CreateView, UpdateView


from .models import Author, Book, Publisher, Store


def index(request):

    return render(request, 'index.html')


def books_list(request):
    books_and_authors = Book.objects.prefetch_related('authors').all()

    return render(request, 'books.html', {'books_and_authors': books_and_authors})


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.prefetch_related('authors', 'stores_books').select_related('publisher').all(),
        pk=pk)

    return render(request, 'bookdetail.html', {'book': book})


class AuthorList(generic.ListView):
    model = Author
    paginate_by = 4
    queryset = Author.objects.all().annotate(Count('books_auths'))
#
# def authors_list(request):
#     authors_and_books_amt = Author.objects.all().annotate(Count('books_auths'))
#
#     return render(request, 'authors.html', {'authors_and_books_amt': authors_and_books_amt})


class AuthorDetail(generic.DetailView):
    model = Author


def publishers_list(request):
    pubs_books_and_stuff = Publisher.objects.all().annotate(Count('books_pubs')).annotate(Avg('books_pubs__rating'))

    return render(request, 'publishers.html', {'pubs_books_and_stuff': pubs_books_and_stuff})


def publisher_detail(request, pk):
    pubbie = get_object_or_404(
        Publisher.objects.prefetch_related('books_pubs', 'books_pubs__authors').all().annotate(Count('books_pubs')),
        pk=pk,
    )

    return render(request, 'publisherdetail.html', {'pubbie': pubbie})


def stores_list(request):
    stores_books = Store.objects.prefetch_related('books').all().annotate(Count('books')).annotate(Avg('books__price'))

    return render(request, 'stores.html', {'stores_books': stores_books})


def store_detail(request, pk):
    store = get_object_or_404(
        Store.objects.prefetch_related('books', 'books__authors').all().annotate(Count('books')),
        pk=pk,
    )

    return render(request, 'storedetail.html', {'store': store})


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books_and_folks:authors')


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books_and_folks:authors')


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('books_and_folks:authors')
