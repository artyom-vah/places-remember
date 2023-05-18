from django.contrib import admin
from .models import *

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'description', 'author')
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')