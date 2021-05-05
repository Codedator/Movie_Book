from django.urls import path
from . import views

app_name = 'search_movie'
urlpatterns = [
    path('select_city/', views.search_city, name='select_city'),
]
