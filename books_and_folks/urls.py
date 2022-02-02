from django.urls import path

from . import views

app_name = 'books_and_folks'
urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('book/<int:pk>/', views.book_detail, name='book'),
    path('books/', views.books_list, name='books'),
    path('publisher/<int:pk>/', views.publisher_detail, name='publisher'),
    path('publishers/', views.publishers_list, name='publishers'),
    path('store/<int:pk>/', views.store_detail, name='store'),
    path('stores/', views.stores_list, name='stores'),
]
