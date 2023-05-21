from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal

from memories.models import Place


class PlaceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Artyom')
        self.place = Place.objects.create(
            title='Россия',
            description='Описание России',
            author=self.user,
            latitude=Decimal('55.7558'),
            longitude=Decimal('37.6176')
        )

    def test_create_place(self):
        """Проверка создания экземпляра модели Place."""
        self.assertEqual(self.place.title, 'Россия')
        self.assertEqual(self.place.description, 'Описание России')
        self.assertEqual(self.place.author, self.user)

    def test_pub_date_auto_filled(self):
        """Проверка автоматического заполнения поля pub_date."""
        self.assertIsNotNone(self.place.pub_date)

    def test_save_method_geocoding(self):
        """Проверка выполнения геокодирования при сохранении без координат."""
        place = Place.objects.create(
            title='Россия',
            description='Описание России',
            author=self.user
        )
        place.save()
        self.assertIsNotNone(place.latitude)
        self.assertIsNotNone(place.longitude)

    def test_str_representation(self):
        """Проверка строкового представления экземпляра модели."""
        self.assertEqual(str(self.place), 'Россия')

    def test_sorting_order(self):
        """Проверка порядка сортировки."""
        place2 = Place.objects.create(
            title='Место 2',
            description='Описание места 2',
            author=self.user
        )
        place3 = Place.objects.create(
            title='Место 3',
            description='Описание места 3',
            author=self.user
        )
        places = Place.objects.all()
        self.assertEqual(list(places), [place3, place2, self.place])

