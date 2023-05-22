from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddPlaceForm
from .models import Place
from .utils import create_marker_list, get_vk_account_data


def index(request: HttpRequest) -> HttpResponse:
    '''Главная страница'''
    return render(request, 'memories/index.html')


@login_required
def list_places(request: HttpRequest) -> HttpResponse:
    '''Список всех мест, где побывал пользователь'''
    places = Place.objects.filter(author=request.user)
    first_name, last_name = get_vk_account_data(request.user)
    context = {
        'places': places,
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, 'memories/list_places.html', context)


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
    map = create_marker_list(request.user)
    context = {
        'form': form,
        'map': map,
    }
    return render(request, 'memories/add_place.html', context)
