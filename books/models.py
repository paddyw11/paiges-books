from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    sku = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField()
    number_of_pages = models.IntegerField()
    genre_category = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    release_date = models.DateField()
    image_url = models.URLField(null=True, blank=True)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.title