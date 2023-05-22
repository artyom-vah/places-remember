import folium
from allauth.socialaccount.models import SocialAccount

from .models import Place, User


def create_marker_list(user: User):
    ''' Создает карту с маркерами для всех мест пользователя.'''
    # Получаем все места пользователя, выбирая только поле "название"
    addresses = Place.objects.filter(author=user).only('title')
    marker_list = []
    # Проходим по каждому месту
    for address in addresses:
        # Проверяем, есть ли значения широты и долготы у данного места
        if address.latitude and address.longitude:
            # Если есть, добавляем координаты в список маркеров
            marker_list.append([address.latitude, address.longitude])
    # Создаем объект карты folium с начальным зумом 10 и предпочтением
    # использовать canvas canvas - может быть более производительным и
    # позволять плавную анимацию и интерактивность на карте
    map = folium.Map(zoom_start=10, prefer_canvas=True)
    # Добавляем каждый маркер на карту
    for marker in marker_list:
        folium.Marker(marker).add_to(map)
    # map_html = m.get_root().render() # сбрасывает стили бутстрапа(
    return map._repr_html_()


def get_vk_account_data(user: User):
    vk_account = None
    try:
        vk_account = user.socialaccount_set.get(provider='vk')
        first_name = vk_account.extra_data['first_name']
        last_name = vk_account.extra_data['last_name']
    except SocialAccount.DoesNotExist:
        first_name = ''
        last_name = ''
    return first_name, last_name
