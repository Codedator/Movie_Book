from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def search_city(request):
    city_list = City.objects.values_list('city_name', flat=True).all().order_by('city_name')
    context = {'city_list': city_list}
    return render(request, 'search_movie/movie_search.html', context)
