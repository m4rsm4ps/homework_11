from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render

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


def authors_list(request):
    authors_and_books_amt = Author.objects.all().annotate(Count('books_auths'))

    return render(request, 'authors.html', {'authors_and_books_amt': authors_and_books_amt})


def author_detail(request, pk):
    author = get_object_or_404(
        Author.objects.prefetch_related('books_auths').all().annotate(Count('books_auths')),
        pk=pk,
    )

    return render(request, 'authordetail.html', {'author': author})


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
