from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Place
from .forms import AddPlaceForm
from allauth.socialaccount.models import SocialAccount
import folium


def index(request: HttpRequest) -> HttpResponse:
    '''Главная страница''' 
    return render(request, 'memories/index.html')


@login_required
def list_places(request: HttpRequest) -> HttpResponse:
    '''Список всех мест, где пользователь был'''
    # places = Place.objects.all()
    
    places = Place.objects.filter(author=request.user)
    vk_account = None
    
    try:
        vk_account = request.user.socialaccount_set.get(provider='vk')
        first_name = vk_account.extra_data['first_name']
        last_name = vk_account.extra_data['last_name']
    except SocialAccount.DoesNotExist:
        # В случае отсутствия у пользователя социальной учетной записи VK
        first_name = ''
        last_name = ''
        
    context = {
        'places': places,
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, 'memories/list_places.html', context)



# @login_required
# def add_place(request: HttpRequest) -> HttpResponse:
#     '''Добавить новое место'''
#     if request.method == 'POST':
#         form = AddPlaceForm(request.POST)
#         if form.is_valid():
#             place = form.save(commit=False)            
#             place.author = request.user
#             print(request.user)
#             form.save()
#             return redirect('memories:list_places')
#             # Создание экземпляра карты Folium
#             my_map = folium.Map(location=[place.latitude, place.longitude], zoom_start=12)

#             # Добавление маркера на карту
#             folium.Marker([place.latitude, place.longitude], popup=place.title).add_to(my_map)
            
#             map_html = my_map.get_root().render()
#     else:
#         form = AddPlaceForm()
#     context = {
#         'form': form,
#         'map_html': map_html
#     }    
#     return render(request, 'memories/add_place.html', context)

@login_required
def add_place(request: HttpRequest) -> HttpResponse:
    '''Добавить новое место'''
    if request.method == 'POST':
        form = AddPlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)            
            place.author = request.user
            form.save()

            # Создание экземпляра карты Folium
            my_map = folium.Map(location=[place.latitude, place.longitude], zoom_start=12)

            # Добавление маркера на карту
            folium.Marker([place.latitude, place.longitude], popup=place.title).add_to(my_map)

            # Получение HTML-кода карты
            map_html = my_map.get_root().render()
            context = {
                'form': form,
                'map_html': map_html
            }
            return render(request, 'memories/add_place.html', context)
    else:
        form = AddPlaceForm()
    context = {
        'form': form,
    }    
    return render(request, 'memories/add_place.html', context)

