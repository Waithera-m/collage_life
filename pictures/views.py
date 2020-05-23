from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def index(request):
    """
    view function returns the landing page
    """
    images = Image.objects.all()
    return render(request, 'all_pictures/index.html', {'images':images})

def animals(request):
    """
    view function returns template that displays animal photos
    """
    images = Image.search_images_by_category(category_id=8)
    return render(request, 'all_pictures/animals.html', {'images':images})

def wedding(request):
    """
    view function renders template that displays vacation photos
    """
    images = Image.search_images_by_category(category_id=4)
    return render(request, 'all_pictures/wedding.html', {'images':images})

def artistic(request):
    """
    view function renders template that displays vacation photos
    """
    images = Image.search_images_by_category(category_id=1)
    return render(request, 'all_pictures/artistic.html', {'images':images})

def vacation(request):
    """
    view function renders template that displays vacation photos
    """
    images = Image.search_images_by_category(category_id=3)
    return render(request, 'all_pictures/vacation.html', {'images':images})

