from django.db import models


class Genre(models.Model):
    nama = models.CharField(max_length=250)

    def __str__(self):
        return self.nama


class Premiered(models.Model):
    MUSIM_CHOICES = (
        ('Spring', 'SPRING'),
        ('Summer', 'SUMMER'),
        ('Fall', 'FALL'),
        ('Winter', 'WINTER')
    )
    musim = models.CharField(
        max_length=250, choices=MUSIM_CHOICES, default='Spring')
    tahun = models.CharField(max_length=4)

    def __str__(self):
        return self.musim + ('%s') % str(self.tahun)


class Type(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Studio(models.Model):
    studio = models.CharField(max_length=200)

    def __str__(self):
        return self.studio


class Status(models.Model):
    STATUS_CHOICES = (
        ('Ongoing', 'ONGOING'),
        ('Complete', 'COMPLETE'),
    )

    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Ongoing')

    def __str__(self):
        return self.status


class Series(models.Model):
    series = models.CharField(max_length=200)

    def __str__(self):
        return self.series

class Layanan(models.Model):
    layanan = models.CharField(max_length=200)

    def __str__(self):
        return self.layanan


class Anime(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/covers/')
    sampul = models.ImageField(upload_to='static/sampul/')
    synonym = models.CharField(max_length=250)
    duration = models.IntegerField()
    premier = models.ForeignKey(Premiered, on_delete=models.CASCADE)
    type_anime = models.ForeignKey(Type, on_delete=models.CASCADE)
    score = models.CharField(max_length=4)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    sinopsis = models.TextField(default="")

    def __str__(self):
        return self.title


class AnimeGenre(models.Model):
    animeId = models.ForeignKey(Anime, on_delete=models.CASCADE)
    genreId = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.animeId)


class EpisodeAnime(models.Model):
    animeId = models.ForeignKey(Anime,on_delete=models.CASCADE)
    episode = models.CharField(max_length=200)

    def __str__(self):
        return  '(%s)' % self.episode + str(self.animeId)

class ResolusiDownloads(models.Model):
    animeId = models.ForeignKey(Anime,on_delete=models.CASCADE)
    episodeAnimeId = models.ForeignKey(EpisodeAnime,on_delete=models.CASCADE)
    resolusi = models.CharField(max_length=10)
    
    def __str__(self):
        return self.resolusi

class LayananDownload(models.Model):
    animeId = models.ForeignKey(Anime,on_delete=models.CASCADE)
    episodeAnimeId = models.ForeignKey(EpisodeAnime,on_delete=models.CASCADE)
    resolusiDownloadId = models.ForeignKey(ResolusiDownloads,on_delete=models.CASCADE)
    layananId = models.ForeignKey(Layanan,on_delete=models.CASCADE)
    link = models.CharField(max_length=250)

    def __str__(self):
        return '(%s)' % self.layananId + ' - ' + '(%s)'% self.animeId + ' - ' + self.link 

