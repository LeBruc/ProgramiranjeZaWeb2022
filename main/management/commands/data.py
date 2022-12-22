from django.db import transaction
from django.core.management.base import BaseCommand
import random
from main.models import*
from main.factory import *

NUM_REDATELJ=10
NUM_GLUMAC=50
NUM_STUDIO=5
NUM_OSOBLJE=100
NUM_REKLAMA=20
NUM_FILM=30
NUM_SERIJA=15

class Command(BaseCommand):
    @transaction.atomic
    def handle(self,*args,**kwargs):
        models=[Redatelj,Glumac,Studio,Osoblje,Reklama,Film,Serija]

        print("delete")
        for m in models:
            m.objects.all().delete()

        print("write")
        for _ in range(NUM_REDATELJ):
            redatelj=RedateljFactory()

        for _ in range(NUM_GLUMAC):
            glumac=GlumacFactory()

        for _ in range(NUM_STUDIO):
            studio=StudioFactory()

        for _ in range(NUM_OSOBLJE):
            osoblje=OsobljeFactory()

        for _ in range(NUM_REKLAMA):
            reklama=ReklamaFactory()

        for _ in range(NUM_FILM):
            film=FilmFactory()

        for _ in range(NUM_SERIJA):
            serija=SerijaFactory()
