from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import Redatelj,Glumac,Studio,Osoblje,Reklama,Film,Serija

def homepage(request):
    return render(request, "base_generic.html")
    
class RedateljList(ListView):
    model=Redatelj

class GlumacList(ListView):
    model=Glumac

class StudioList(ListView):
    model=Studio

class OsobljeList(ListView):
    model=Osoblje

class ReklamaList(ListView):
    model=Reklama

class FilmList(ListView):
    model=Film

class SerijaList(ListView):
    model=Serija