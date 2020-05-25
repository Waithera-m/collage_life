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
    path('dubai_results/', views.dubai_results, name='dubai_results'),
    path('bangkok_results/', views.bangkok_results, name='bangkok_results'),
    path('new_york_results/', views.new_york_results, name='new_york_results'),
    path('amboseli_results/', views.amboseli_results, name='amboseli_results'),
    path('fiji_results/', views.fiji_results, name='fiji_results'),
    path('vanuatu_results/', views.vanuatu_results, name='vanuatu_results'),
    path('malindi_results/', views.malindi_results, name='malindi_results'),
    path('tsavo_results/', views.tsavo_results, name='tsavo_results'),
    path('nairobi_results/', views.nairobi_results, name='nairobi_results'),
    path('west_africa_results/', views.west_africa_results, name='west_africa_results'),
    path('japan_results/', views.japan_results, name='japan_results'),
    path('search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
