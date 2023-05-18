from django.urls import path
from . views import index, list_places, add_place

app_name = 'memories'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list_places, name='list_places'), 
    path('add/', add_place, name='add_place'),
]
