from django.urls import path, include
from . import views
from main.views import RedateljList,GlumacList,StudioList,OsobljeList,ReklamaList,FilmList,SerijaList

app_name='main'

urlpatterns=[
    path('', views.homepage,name='homepage'),
    path('redatelj',RedateljList.as_view()),
    path('glumac',GlumacList.as_view()),
    path('studio',StudioList.as_view()),
    path('osoblje',OsobljeList.as_view()),
    path('reklama',ReklamaList.as_view()),
    path('film',FilmList.as_view()),
    path('serija',SerijaList.as_view()),
]