from django.shortcuts import render

# Create your views here.
def index(request):

    """
    view function returns the landing page
    """
    return render(request,'all_pictures/index.html')