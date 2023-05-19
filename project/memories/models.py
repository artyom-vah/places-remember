from django.contrib.auth import get_user_model
from django.db import models

FIRST_TEXT_STR_15 = 15

User = get_user_model()


class Place(models.Model):
    '''Название места'''
    title = models.CharField(verbose_name='Название места', max_length=200)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, )
    description = models.TextField(verbose_name='Описание места')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place',
                               verbose_name='Автор')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Название места'
        verbose_name_plural = 'Название мест'

    def __str__(self):
        return self.title[:FIRST_TEXT_STR_15]