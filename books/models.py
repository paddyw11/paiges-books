from django.db import models

# Create your models here.
class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'Genres'

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
    genres = models.ManyToManyField('Genre')
    release_date = models.DateField()
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.title