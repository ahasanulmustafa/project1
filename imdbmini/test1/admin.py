from django.contrib import admin
from .models import UserModel, Person, Film, Cast


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'age', 'country']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'poster', 'is_released']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'film', 'film_char']


