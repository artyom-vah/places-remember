from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Place
from .forms import AddPlaceForm


def index(request: HttpRequest) -> HttpResponse:
    '''Главная страница''' 
    return render(request, 'memories/index.html')


@login_required
def list_places(request: HttpRequest) -> HttpResponse:
    '''список мест'''
    places = Place.objects.all()
    context = {
        'places': places,
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
            print(request.user)
            form.save()
            return redirect('memories:list_places')
    else:
        form = AddPlaceForm()
    context = {
        'form': form,
    }    
    return render(request, 'memories/add_place.html', context)
