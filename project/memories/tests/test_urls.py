from http import HTTPStatus

from django.core.cache import cache
from django.test import Client, TestCase
from memories.models import Place, User


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

    def test_index_url(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200

    def test_list_url_authorized_client(self):
        """Страница /list/ доступна авторизованному пользователю."""
        response = self.authorized_client.get('/list/')
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200

    def test_list_url_guest_client(self):
        """Страница /list/ недоступна неавторизованному пользователю."""
        response = self.guest_client.get('/list/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # 302

    def test_add_url_authorized_client(self):
        """Страница /add/ доступна авторизованному пользователю."""
        response = self.authorized_client.get('/add/')
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200

    def test_add_url_guest_client(self):
        """Страница /add/ недоступна неавторизованному пользователю."""
        response = self.guest_client.get('/add/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # 302

    def test_urls_place_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/': 'memories/index.html',
            '/list/': 'memories/list_places.html',
            '/add/': 'memories/add_place.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_page_404(self):
        '''Проверяем несуществующую страницу'''
        response = self.guest_client.get('/page404/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)  # 404
