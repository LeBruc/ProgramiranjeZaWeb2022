from django.db import models
from django.db.models.base import Model

# Create your models here.

class Redatelj(models.Model):
    redatelj_ime = models.CharField(max_length=50)
    redatelj_prezime = models.CharField(max_length=50)
    redatelj_datum_rodenja = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.redatelj_prezime

class Glumac(models.Model):
    glumac_ime = models.CharField(max_length=50)
    glumac_prezime = models.CharField(max_length=50)
    glumac_datum_rodenja = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.glumac_prezime
       


class Studio(models.Model):
    studio_ime = models.CharField(max_length=50)
    datum_osnivanja = models.CharField(max_length=4)

    def __str__(self):
        return self.studio_ime


class Osoblje(models.Model):
    osoblje_ime = models.CharField(max_length=50)
    osoblje_prezime = models.CharField(max_length=50)
    osoblje_uloga = models.CharField(max_length=50)

    def __str__(self):
        return self.osoblje_ime



class Reklama(models.Model):
    reklama_izdavac = models.CharField(max_length=50)
    reklama_trajanje = models.IntegerField(default=1)

    def __str__(self):
        return self.reklama_izdavac



class Film(models.Model):
    film_ime = models.CharField(max_length=100)
    film_datum_objave = models.DateField(null=True,blank=True)
    film_zanr = models.CharField(max_length=30)
    film_ocjena = models.IntegerField(default=1)
    film_budzet = models.IntegerField(default=1)
    film_drzava_proizvodnje = models.CharField(max_length=50)

    redatelj= models.ForeignKey(Redatelj, default=1, on_delete=models.CASCADE,)
    studio= models.ForeignKey(Studio, default=1, on_delete=models.CASCADE,)
    reklama= models.ForeignKey(Reklama, default=1, on_delete=models.CASCADE,)
    glumac= models.ManyToManyField(Glumac)
    osoblje= models.ManyToManyField(Osoblje)




    def __str__(self):
        return self.film_ime

class Serija(models.Model):
    serija_ime = models.CharField(max_length=100)
    serija_datum_objave = models.DateField(null=True,blank=True)
    serija_zanr = models.CharField(max_length=30)
    serija_ocjena = models.IntegerField(default=1)
    serija_budzet = models.IntegerField(default=1)
    serija_drzava_proizvodnje = models.CharField(max_length=50)

    redatelj= models.ForeignKey(Redatelj, default=1, on_delete=models.CASCADE,)
    studio= models.ForeignKey(Studio, default=1, on_delete=models.CASCADE,)
    reklama= models.ForeignKey(Reklama, default=1, on_delete=models.CASCADE,)
    glumac= models.ManyToManyField(Glumac)
    osoblje= models.ManyToManyField(Osoblje)


    def __str__(self):
        return self.serija_ime