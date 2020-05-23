from django.contrib import admin
from .models import Image, Category, Location
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    """
    class facilitates the creation of admin page objects
    """
    fields = ['image_name', 'image_description', 'location', 'category', 'pub_date', 'owner', 'image']
    list_display = ('image_name', 'pub_date')
    list_filter = ['pub_date']
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)
