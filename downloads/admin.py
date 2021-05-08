from django.contrib import admin
from .models import Genre, Premiered, Type, Studio, Status, Series, Anime, AnimeGenre

# Register your models here.
admin.site.register(Genre)
admin.site.register(Premiered)
admin.site.register(Type)
admin.site.register(Studio)
admin.site.register(Status)
admin.site.register(Series)
admin.site.register(Anime)
admin.site.register(AnimeGenre)
