from django.db import models

class Author(models.Model):
    """
    Author data model
    """
    name = models.CharField(max_length=254, unique=True)
    nationality = models.CharField(max_length=254)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)

