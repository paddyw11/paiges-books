from django.urls import path
from . import views
"""
urls.py for books app
"""
urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('offers/', views.books_on_offer, name='books_on_offer'),
    path('bookmark/<int:book_id>/', views.bookmark_add, name='bookmark')
]
