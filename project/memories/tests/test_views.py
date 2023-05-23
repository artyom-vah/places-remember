
from http import HTTPStatus

from allauth.socialaccount.models import SocialAccount
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from memories.forms import AddPlaceForm
from memories.models import Place, User


class ListPlacesViewTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Artyom')
        cls.other_user = User.objects.create_user(username='John')
        # Создадим записи в БД для проверки доступности адресов
        cls.place = Place.objects.create(
            title='Россия',
            description='Описание России',
            author=cls.user,
        )
        cls.other_place = Place.objects.create(
            title='США',
            description='Описание США',
            author=cls.other_user,
        )
        cls.vk_account = SocialAccount.objects.create(
            user=cls.user,
            provider='vk',
            extra_data={
                'first_name': 'Art',
                'last_name': 'Vah'
            }
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

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

    def test_list_places_page_show_correct_context(self):
        """Шаблон list_places сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse('memories:list_places'))
        place_list = response.context.get('places')
        place_list_expected = Place.objects.filter(author=self.user)
        self.assertQuerysetEqual(place_list, place_list_expected,
                                 transform=lambda x: x)

    def test_list_places_page_requires_authentication(self):
        """Проверка, что доступ к странице требует аутентификации."""
        response = self.guest_client.get(reverse('memories:list_places'))
        self.assertIn(response.status_code, (HTTPStatus.FOUND,
                                             HTTPStatus.FORBIDDEN))  # 302, 403

    def test_list_places_page_show_only_user_places(self):
        """Проверка, что список мест отображается только для текущего
        пользователя."""
        response = self.authorized_client.get(reverse('memories:list_places'))
        place_list = response.context['places']
        self.assertEqual(len(place_list), 1)
        self.assertEqual(place_list[0], self.place)

    def test_list_places_page_displays_social_account_info(self):
        """Проверка, что информация о социальной учетной записи VK
        отображается в контексте страницы."""
        response = self.authorized_client.get(reverse('memories:list_places'))
        first_name = response.context['first_name']
        last_name = response.context['last_name']
        self.assertEqual(first_name, 'Art')
        self.assertEqual(last_name, 'Vah')

    def test_list_places_page_without_social_account_info(self):
        """Проверка, что соответствующие поля контекста пустые при отсутствии
        социальной учетной записи VK."""
        SocialAccount.objects.all().delete()
        response = self.authorized_client.get(reverse('memories:list_places'))
        first_name = response.context['first_name']
        last_name = response.context['last_name']
        self.assertEqual(first_name, '')
        self.assertEqual(last_name, '')

    def test_list_places_page_displays_places_in_correct_order(self):
        """Проверка, что список мест отображается в правильном порядке."""
        Place.objects.create(
            title='Франция',
            description='Описание Франции',
            author=self.user,
        )
        Place.objects.create(
            title='Германия',
            description='Описание Германии',
            author=self.user,
        )
        response = self.authorized_client.get(reverse('memories:list_places'))
        place_list = response.context['places']
        expected_order = ['Германия', 'Франция', 'Россия']
        self.assertQuerysetEqual(place_list, expected_order,
                                 transform=lambda x: x.title)


class AddPlaceViewTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(username='Artyom')

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_add_place_view_with_get_request(self):
        """Проверка доступности страницы добавления места с GET-запросом."""
        response = self.authorized_client.get(reverse('memories:add_place'))
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200
        self.assertTemplateUsed(response, 'memories/add_place.html')
        self.assertIsInstance(response.context['form'], AddPlaceForm)

    def test_add_place_view_with_post_request(self):
        """Проверка добавления места с POST-запросом."""
        form_data = {
            'title': 'Место 1',
            'description': 'Описание места 1',
        }
        response = self.authorized_client.post(reverse('memories:add_place'),
                                               data=form_data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200
        self.assertTemplateUsed(response, 'memories/list_places.html')
        self.assertRedirects(response, reverse('memories:list_places'))
        self.assertEqual(Place.objects.count(), 1)
        place = Place.objects.first()
        self.assertEqual(place.title, 'Место 1')
        self.assertEqual(place.description, 'Описание места 1')
        self.assertEqual(place.author, self.user)

    def test_add_place_view_with_invalid_form(self):
        """Проверка добавления места с недопустимой формой."""
        form_data = {
            'title': '',
            'description': 'Описание места 1',
        }
        response = self.authorized_client.post(reverse('memories:add_place'),
                                               data=form_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200
        self.assertTemplateUsed(response, 'memories/add_place.html')
        self.assertIsInstance(response.context['form'], AddPlaceForm)
        self.assertEqual(Place.objects.count(), 0)
