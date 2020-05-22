from django.db import models

# Create your models here.
class Location(models.Model):

    """
    class facilitates the creation of location objects
    """
    location_name = models.CharField(max_length=70)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    
    """
    class facilitates the creation of category objects
    """
    category_name = models.CharField(max_length=70)

    def __str__(self):
        return self.category_name

class Image(models.Model):

    """
    class facilitates the creation of image objects
    """
    image_name = models.CharField(max_length=70)
    image_description = models.TextField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name


