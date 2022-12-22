import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from main.models import *



class RedateljFactory(DjangoModelFactory):
    class Meta:
        model=Redatelj
    
    redatelj_ime=factory.Faker("first_name")
    redatelj_prezime=factory.Faker("last_name")
    redatelj_datum_rodenja=factory.Faker("date_of_birth")


class GlumacFactory(DjangoModelFactory):
    class Meta:
        model=Glumac

    glumac_ime=factory.Faker("first_name")
    glumac_prezime=factory.Faker("last_name")
    glumac_datum_rodenja=factory.Faker("date_of_birth")

class StudioFactory(DjangoModelFactory):
    class Meta:
        model=Studio

    studio_ime=factory.Faker("company")
    datum_osnivanja=factory.Faker("date_of_birth")

class OsobljeFactory(DjangoModelFactory):
    class Meta:
        model=Osoblje

    osoblje_ime=factory.Faker("first_name")
    osoblje_prezime=factory.Faker("last_name")
    osoblje_uloga=factory.Faker("job")

class ReklamaFactory(DjangoModelFactory):
    class Meta:
        model=Reklama

    reklama_izdavac=factory.Faker("company")
    reklama_trajanje=factory.fuzzy.FuzzyInteger(1,5)

class FilmFactory(DjangoModelFactory):
    class Meta:
        model=Film

    film_ime=factory.Faker("word")
    film_datum_objave=factory.Faker("date_of_birth")
    film_zanr=factory.Faker("word")
    film_ocjena=factory.fuzzy.FuzzyInteger(1,10)
    film_budzet=factory.fuzzy.FuzzyInteger(1,10000000)
    film_drzava_proizvodnje=factory.Faker("country")

    redatelj=factory.Iterator(Redatelj.objects.all())
    studio=factory.Iterator(Studio.objects.all())
    reklama=factory.Iterator(Reklama.objects.all())

    @factory.post_generation
    def glumacs(self,create,extracted,**kwargs):
        if not create:
            return
        if extracted:
            for glumac in extracted:
                self.glumacs.add(glumac)

    @factory.post_generation
    def osobljes(self,create,extracted,**kwargs):
        if not create:
            return
        if extracted:
            for osoblje in extracted:
                self.osobljes.add(osoblje)


class SerijaFactory(DjangoModelFactory):
    class Meta:
        model=Serija
    
    serija_ime=factory.Faker("word")
    serija_datum_objave=factory.Faker("date_of_birth")
    serija_zanr=factory.Faker("word")
    serija_ocjena=factory.fuzzy.FuzzyInteger(1,10)
    serija_budzet=factory.fuzzy.FuzzyInteger(1,50000000)
    serija_drzava_proizvodnje=factory.Faker("country")

    redatelj=factory.Iterator(Redatelj.objects.all())
    studio=factory.Iterator(Studio.objects.all())
    reklama=factory.Iterator(Reklama.objects.all())

    @factory.post_generation
    def glumacs(self,create,extracted,**kwargs):
        if not create:
            return
        if extracted:
            for glumac in extracted:
                self.glumacs.add(glumac)

    @factory.post_generation
    def osobljes(self,create,extracted,**kwargs):
        if not create:
            return
        if extracted:
            for osoblje in extracted:
                self.osobljes.add(osoblje)

