from django.shortcuts import render
from .models import Anime

# Create your views here.


def index(request):
    animelist = Anime.objects.all()
    content = {
        'animelist': animelist,
    }
    return render(request, 'index.html', content)
