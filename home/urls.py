from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('faqs/', views.faqs, name='faqs'),
]
