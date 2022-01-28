from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def get_books(self):
        return ', '.join([book.name for book in self.books_auths.all()])

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('publisher-detail', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name='books_auths')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books_pubs')
    pubdate = models.DateField()

    def __str__(self):
        return self.name

    def get_authors(self,):
        return ', '.join([author.name for author in self.authors.all()])


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book, related_name='stores_books')

    def __str__(self):
        return self.name
