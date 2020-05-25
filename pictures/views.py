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

def get_results(request):
    """
    view function returns search by location results
    """
    images = Image.filter_images_by_location(location_id=1)
    
    return render(request, 'all_pictures/search.html', {"images":images})

def dubai_results(request):
    """
    view function returns template that displays Dubai-specific photos
    """
    images = Image.filter_images_by_location(location_id=2)

    return render(request, "all_pictures/dubai.html", {"images":images})

def bangkok_results(request):
    """
    view function returns template that displays Bangkok-specific photos
    """
    images = Image.filter_images_by_location(location_id=3)

    return render(request, "all_pictures/bangkok.html", {"images":images})

def new_york_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=4)
    return render(request, "all_pictures/new_york.html", {"images":images})

def amboseli_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=5)
    return render(request, "all_pictures/amboseli.html", {"images":images})

def fiji_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=6)
    return render(request, "all_pictures/fiji.html", {"images":images})

def vanuatu_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=7)
    return render(request, "all_pictures/vanuatu.html", {"images":images})

def malindi_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=8)
    return render(request, "all_pictures/malindi.html", {"images":images})

def tsavo_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=9)
    return render(request, "all_pictures/tsavo.html", {"images":images})

def nairobi_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=10)
    return render(request, "all_pictures/nairobi.html", {"images":images})

def west_africa_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=11)
    return render(request, "all_pictures/west_africa.html", {"images":images})

def japan_results(request):
    """
    view function returns template that displays New York-specific photos
    """
    images = Image.filter_images_by_location(location_id=12)
    return render(request, "all_pictures/japan.html", {"images":images})

