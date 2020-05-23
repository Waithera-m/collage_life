from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def index(request):

    """
    view function returns the landing page
    """
    images = Image.objects.all()
    return render(request, 'all_pictures/index.html', {'images':images})