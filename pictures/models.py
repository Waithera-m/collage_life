from django.db import models

# Create your models here.
class Location(models.Model):

    """
    class facilitates the creation of location objects
    """
    location_name = models.CharField(max_length=70)

    def __str__(self):
        return self.location_name

    def save_location(self):

        """
        method saves entered location in database
        """
        self.save()
    
    def update_location(self, using=None, fields=None, **kwargs):
        
        """
        method updates saved location
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)
    
    def delete_location(self):

        """
        method deletes location
        """
        self.delete()

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
    pub_date = models.DateField('date published', null=True)

    def __str__(self):
        return self.image_name

