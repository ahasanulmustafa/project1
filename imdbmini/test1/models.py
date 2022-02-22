from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usermodel')
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Person(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=30)


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    poster = models.ImageField()
    is_released = models.BooleanField(default=True)


class Cast(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
    film_char = models.CharField(max_length=30)

# fil = Film.objects.filter(film__person__user_id=)
# fil = Film.objects.filter(film__person__user_id=1,).filter(is_released=False)

# select * from Film where id in (select film_id from cast where person_id in (select id from person where user_id = 1))
