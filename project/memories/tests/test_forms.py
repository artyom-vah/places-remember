from django.contrib.auth.models import User
from django.test import TestCase
from memories.forms import AddPlaceForm


class AddPlaceFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Artyom')

    def test_form_fields(self):
        """Проверка полей формы."""
        form = AddPlaceForm()
        self.assertEqual(
            list(form.fields.keys()),
            ['title', 'description']
        )
        self.assertEqual(
            form.fields['title'].label,
            'Название места'
        )
        self.assertEqual(
            form.fields['description'].label,
            'Описание места'
        )

    def test_valid_form_data(self):
        """Проверка валидных данных формы."""
        form = AddPlaceForm(data={
            'title': 'Место',
            'description': 'Описание места'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form_data(self):
        """Проверка невалидных данных формы."""
        form = AddPlaceForm(data={
            'title': '',
            'description': ''
        })
        self.assertFalse(form.is_valid())

    def test_form_widgets(self):
        """Проверка виджетов полей формы."""
        form = AddPlaceForm()
        self.assertEqual(
            form.fields['title'].widget.attrs['class'],
            'form-control'
        )
        self.assertEqual(
            form.fields['description'].widget.attrs['class'],
            'form-control'
        )
