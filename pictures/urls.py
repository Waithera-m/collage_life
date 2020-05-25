from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "pictures"

urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.animals, name='animals'),
    path('wedding/', views.wedding, name='wedding'),
    path('artistic/', views.artistic, name='artistic'),
    path('vacation/', views.vacation, name='vacation'),
    path('get_results/', views.get_results, name='get_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
