from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_submit, name='contact_submit'),
    path('', views.contact_us, name='contact_us')
]
