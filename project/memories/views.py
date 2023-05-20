import folium
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddPlaceForm
from .models import Place


def index(request: HttpRequest) -> HttpResponse:
    '''Главная страница''' 
    return render(request, 'memories/index.html')


@login_required
def list_places(request: HttpRequest) -> HttpResponse:
    '''Список всех мест, где побывал пользователь'''    
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


# работает нормально, отмечает все маркеры где был пользовательно но очень долго отрисовывает все
@login_required
def add_place(request: HttpRequest) -> HttpResponse:
    '''Добавить новое место'''
    if request.method == 'POST':
        form = AddPlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            form.save()
            return redirect('memories:list_places')
    else:
        form = AddPlaceForm()

    # addresses = Place.objects.filter(author=request.user).only('latitude', 'longitude')  # Получаем все места пользователя, выбирая только поля широты и долготы
    addresses = Place.objects.filter(author=request.user).only('title')

    marker_list = []  # Создаем пустой список маркеров

    for address in addresses:
        if address.latitude and address.longitude:
            marker_list.append([address.latitude, address.longitude])  # Добавление координат в список marker_list            
 
    m = folium.Map(zoom_start=10)

    for marker in marker_list:
        folium.Marker(marker).add_to(m)

    map = m.get_root().render()
    
    context = {
        'form': form,
        'map': map,
    }
    return render(request, 'memories/add_place.html', context)






