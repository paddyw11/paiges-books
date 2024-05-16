from django.contrib import admin
from .models import Book, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'sku', 
        'title',
        'author',
        'price',
        'offer',
    )

    ordering = ('sku',)
        
# Register your models here.
admin.site.register(Book, BooksAdmin)
admin.site.register(Genre, GenreAdmin)