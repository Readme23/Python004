from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Movies
# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")

def movies(request):
    title = Movies.objects.get(id=44).movie_title
    all_evaluate = Movies.objects.values_list('movie_evaluate').filter(movie_title=title)
    short_evaluate = []
    star_l = []
    # 判断评论星级
    for i in range(len(all_evaluate)):
        if Movies.objects.get(movie_evaluate=all_evaluate[i][0]).movie_star in ['力荐','推荐','一般']:
            short_evaluate.append(all_evaluate[i])
            star = Movies.objects.get(movie_evaluate=all_evaluate[i][0]).movie_star
            star_l.append(star)
        else:
            pass

    return render(request, 'index.html', locals())