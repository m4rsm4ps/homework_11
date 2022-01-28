from django.urls import path

from . import views

app_name = 'books_and_folks'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list, name='books'),
    path('authors/', views.authors_list, name='authors'),
    path('publishers/', views.publishers_list, name='publishers'),
    path('stores/', views.stores_list, name='stores'),
    path('book/<int:pk>/', views.book_detail, name='book'),
    path('author/<int:pk>/', views.author_detail, name='author'),
    path('publisher/<int:pk>/', views.publisher_detail, name='publisher'),
    path('store/<int:pk>/', views.store_detail, name='store'),
]
