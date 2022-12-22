from django.contrib import admin
from main.models import *

model_list=[Redatelj,Glumac,Studio,Osoblje,Reklama,Film,Serija]
admin.site.register(model_list)