from django.contrib import admin

from .models import Author, Book, Publisher, Store


class AuthorshipInline(admin.TabularInline):
    model = Book.authors.through


class ShipmentInline(admin.TabularInline):
    model = Store.books.through


class BookInline(admin.TabularInline):
    model = Book
    exclude = ('books_pubs', 'pages',)
    readonly_fields = ('name', 'authors', 'rating', 'price', 'pubdate',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_authors', 'rating', 'price',)
    fieldsets = (
        (None, {
            'fields': (('name', 'authors'), ('pages', 'rating', 'price'), ('publisher', 'pubdate')),
        }),
    )
    readonly_fields = ('authors',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_books',)
    inlines = [
        AuthorshipInline,
    ]


class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]


class StoreAdmin(admin.ModelAdmin):
    exclude = ('books',)
    inlines = [ShipmentInline]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Store, StoreAdmin)
