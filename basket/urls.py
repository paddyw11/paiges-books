from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('update_quantity/<item_id>/', views.update_quantity, name='update_quantity'),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),

]
