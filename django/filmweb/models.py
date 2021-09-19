from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DodatkoweInfo(models.Model):
    GATUNEK={
        (0,'Inne'),
        (1,'Horror'),
        (2,'Sci-fi'),
        (3,'Komedia'),
        (4,'Drama'),
    }
    czas_trwania=models.PositiveSmallIntegerField(default=0)
    gatunek=models.PositiveSmallIntegerField(default=0,choices=GATUNEK)

class Film(models.Model):
    tytul=models.CharField(max_length=64, blank=False, unique=True)
    rok=models.PositiveSmallIntegerField(default=2000)
    opis=models.TextField(max_length=500, null= False, blank=True)
    premiera=models.DateTimeField(null=True, blank=True)
    imbq_rating=models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    plakat=models.ImageField(upload_to='plakaty',null=False, blank=True)
    dodatkowe=models.OneToOneField(DodatkoweInfo,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.tytul_plus_rok()

    def tytul_plus_rok(self):
        return '{} ({})'.format(self.tytul,self.rok)

class Ocena(models.Model):
    recenzja=models.TextField(default="")
    gwiazdki=models.PositiveSmallIntegerField(default=5)
    film=models.ForeignKey(Film,on_delete=models.CASCADE)

class Aktor(models.Model):
    imie=models.CharField(max_length=32)
    nazwisko=models.CharField(max_length=32)
    film=models.ManyToManyField(Film)

