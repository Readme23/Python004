from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Movies
# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")

def movies(request):
    title = Movies.objects.get(id=44).movie_title
    short_evaluate = Movies.objects.values_list('movie_evaluate').filter(movie_title=title)[0:3]
    star_l = []
    for i in range(3):
        star = Movies.objects.get(movie_evaluate=short_evaluate[i][0]).movie_star
        star_l.append(star)
    
    return render(request, 'index.html', locals())