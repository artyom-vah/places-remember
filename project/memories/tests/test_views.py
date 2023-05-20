from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse
from memories.models import Place

User = get_user_model()

class PlaceModelTests(TestCase):  
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Artyom')
        # Создадим запись в БД для проверки доступности адресов
        Place.objects.create(
            title='Россия',
            description='Описание России',
            author=cls.user,
        )
      
    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        cache.clear()
        
    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_pages_names = {
            reverse('memories:index'): 'memories/index.html',
            reverse('memories:list_places'): 'memories/list_places.html',
            reverse('memories:add_place'): 'memories/add_place.html',
        }
        for reverse_name, template in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
        