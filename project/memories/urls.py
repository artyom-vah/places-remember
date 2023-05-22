from django.urls import path

from .views import add_place, index, list_places

app_name = 'memories'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list_places, name='list_places'),
    path('add/', add_place, name='add_place'),
]
