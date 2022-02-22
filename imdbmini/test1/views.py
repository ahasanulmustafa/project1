import io
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import UserModel, Person, Film, Cast
from .serializers import UserModelSerializer, PersonSerializer, FilmSerializer, CastSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView

# genericAPIView and Model Mixin
from .models import Film
from .serializers import FilmSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from django_filters.rest_framework import DjangoFilterBackend


# UserModel API

class LcUserAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RudUserAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Film API

class LCFilmApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RUDFilmAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Cast API

class LcCastAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
class CastMovieListApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            fil = Film.objects.filter(film__person__user_id=id)
            serializer = FilmSerializer(fil, many=True)
            return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class CastMovieToBeReleasedApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            fil = Film.objects.filter(film__person__user_id=id).filter(is_released=False)
            serializer = FilmSerializer(fil, many=True)
            return Response(serializer.data)


class RudCastAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Person API

class LcPersonAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RudPersonAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def home(request):
    return HttpResponse("Hello Welcome to the IMDB")


def Film_list(request):
    film = Film.objects.all()
    serializer = FilmSerializer(film, many=True)
    return JsonResponse(serializer.data, safe=False)


def Film_details(request, pk):
    details = Film.objects.get(),
    serializer = FilmSerializer(details)
    return JsonResponse(serializer.data, safe=False)

# @permission_classes((permissions.AllowAny,))
# class FilmApi(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             fil = Film.objects.get(pk=id),
#             serializer = FilmSerializer(fil, many=True)
#             return Response(serializer.data)
#         fil = Film.objects.all()
#         serializer = FilmSerializer(fil, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = FilmSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         id = pk
#         fil = Film.objects.get(pk=id)
#         serializer = FilmSerializer(fil, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, format=None):
#         id = pk
#         fil = Film.objects.get(pk=id)
#         serializer = FilmSerializer(fil, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         id = pk
#         fil = Film.objects.get(pk=id)
#         fil.delete()
#         return Response({'msg': 'Data Deleted'})

# @method_decorator(csrf_exempt, name='dispatch')
# class film_api(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None)
#
#         if id is not None:
#             fil = Film.objects.get(id=id)
#             serializer = FilmSerializer(fil)
#             return JsonResponse(serializer.data, safe=False)
#
#         fil = Film.objects.all()
#         serializer = FilmSerializer(fil, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             json_data = request.body
#             print(json_data)
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             serializer = FilmSerializer(data=python_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {"msg": "Data Added"}
#                 return JsonResponse(res, safe=False)
#             return JsonResponse(serializer.errors, safe=False)
#
#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         fil = Film.objects.get(id=id)
#         serializer = FilmSerializer(fil, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": "Data Updated!!!"}
#             return JsonResponse(res, safe=False)
#         return JsonResponse(serializer.errors, safe=False)
#
#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         fil = Film.objects.get(id=id)
#         fil.delete()
#         res = {"msg": "Data Deleted!!"}
#         return JsonResponse(res, safe=False)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# class film_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#
#         if id is not None:
#             fil = Film.objects.get(id=id)
#             serializer = FilmSerializer(fil)
#             return Response(Serializer.data)
#
#         fil = Film.objects.all()
#         serializer = FilmSerializer(fil, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = FilmSerializer(data=request.data)
#         # json_data = request.body
#         # print(json_data)
#         # stream = io.BytesIO(json_data)
#         # python_data = JSONParser().parse(stream)
#         # serializer = FilmSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'data created'})
#         return Response(serializer.errors)
#
#     if request.method == 'PUT':
#         id = request.data.get('id')
#         # json_data = request.body
#         # print(json_data)
#         # stream = io.BytesIO(json_data)
#         # python_data = JSONParser().parse(stream)
#         # id = python_data.get('id')
#         fil = Film.objects.get(pk=id)
#         serializer = FilmSerializer(fil, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Data Updated!!!"})
#         return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         # json_data = request.body
#         # stream = io.BytesIO(json_data)
#         # python_data = JSONParser().parse(stream)
#         # id = python_data.get('id')
#         fil = Film.objects.get(pk=id)
#         fil.delete()
#         return Response({"msg": "Data Deleted!!"})

#
# @csrf_exempt
# def person_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#
#         if id is not None:
#             per = Person.objects.get(id=id)
#             serializer = PersonSerializer(per)
#             return JsonResponse(serializer.data, safe=False)
#         per = Person.objects.all()
#         serializer = PersonSerializer(per)
#         return JsonResponse(serializer.data)
#
#     if request.method == "POST":
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = PersonSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": "Data Updated!!!"}
#             return JsonResponse(res, safe=False)
#         return JsonResponse(serializer.errors, safe=False)
#
#     if request.method == "PUT":
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         per = Person.objects.get(id=id)
#         serializer = PersonSerializer(per, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": "Data Updated!!!"}
#             return JsonResponse(res, safe=False)
#         return JsonResponse(serializer.errors, safe=False)
#
#     if request.method == "DELETE":
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         per = Person.objects.get(id=id)
#         per.delete()
#         res = {"msg": "Item Deleted!!!"}
#         return JsonResponse(res, safe=False)
