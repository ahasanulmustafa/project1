from abc import ABC

from rest_framework import serializers
from .models import UserModel, Person, Film, Cast


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'email', 'password')


class PersonSerializer(serializers.ModelSerializer):
    usermodel = UserModelSerializer(read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'user', 'age', 'country', 'usermodel')

    # def create(self, validated_data):
    #     return Person.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     print(instance.user)
    #     instance.user = validated_data.get('user', instance.user)
    #     print(instance.user)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.save()
    #     return instance


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'release_date', 'poster', 'is_released']

    # def create(self, validated_data):
    #     return Film.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     print(instance.title)
    #     instance.title = validated_data.get('title', instance.title)
    #     print(instance.title)
    #     instance.release_date = validated_data.get('release_date', instance.release_date)
    #     instance.poster = validated_data.get('poster', instance.poster)
    #     instance.is_release = validated_data.get('is_released', instance.is_released)
    #     instance.save()
    #     return instance


class CastSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = Cast
        fields = ('id', 'person', 'film', 'film_char')
