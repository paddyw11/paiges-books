from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:author_id>/', views.author_bio, name='author_bio'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<int:author_id>/', views.edit_author, name='edit_author'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
]