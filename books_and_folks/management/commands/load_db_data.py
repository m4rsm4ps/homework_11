import decimal
import random

from books_and_folks.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    """
    This command creates 10 Publishers, 20 Authors, 100 Books and 30 Stores
    and sets relationships between them
    in a very ugly and inefficient way...
    """

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        for p in range(1, 11):
            Publisher(name=f'Publisher_{p}').save()

        for a in range(1, 21):
            Author(name=f'Author_{a}', age=random.randint(4, 124)).save()

        all_authors = Author.objects.all()

        for s in range(1, 31):
            Store(name=f'Store_{s}').save()

        for b in range(1, 101):
            Book(
                name=f'Book_{b}',
                pages=random.randint(10, 1000),
                price=decimal.Decimal(random.randrange(10000))/100,
                rating=round(random.uniform(1, 5.01), 1),
                publisher=Publisher.objects.get(name=f'Publisher_{random.randint(1, 10)}'),
                pubdate=timezone.localdate(),
            ).save()

        bookies = Book.objects.all()

        for book in bookies:
            if int(book.pk) % random.randint(7, 42) == 0:
                list_authors = list(Author.objects.all())
                for i in range(random.randint(2, 4)):
                    book.authors.add(list_authors.pop(random.randint(0, 15)))
            else:
                book.authors.add(all_authors[random.randint(0, 19)])

        for store in Store.objects.all():
            for i in range(1, random.randint(19, 31)):
                store.books.add(bookies[random.randint(0, 99)])
