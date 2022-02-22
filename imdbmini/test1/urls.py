from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('film_list/', views.Film_list, name='film_list'),
   path('film_list/<int:pk>', views.Film_details, name='film_details'),
   # path('filmapi/', views.FilmApi.as_view()),
   # path('filmapi/<int:pk>', views.FilmApi.as_view()),
   path('filmlist/', views.LCFilmApi.as_view()),
   path('filmlist/<int:pk>', views.RUDFilmAPI.as_view()),
   path('castlist/', views.LcCastAPI.as_view()),
   path('castlist/<int:pk>', views.RudCastAPI.as_view()),
   path('personlist/', views.LcPersonAPI.as_view()),
   path('personlist/<int:pk>', views.RudPersonAPI.as_view()),
   path('user/', views.LcUserAPI.as_view()),
   path('user/<int:pk>', views.RudUserAPI.as_view()),
   path('castmovie/<int:pk>', views.CastMovieListApi.as_view()),
   path('castupcoming/<int:pk>', views.CastMovieToBeReleasedApi.as_view()),
   # path('try/', views.CreateUserAPI.as_view()),


]

