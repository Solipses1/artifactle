from django.contrib import admin
from .models import Artifact, Museum, Country, Game

# Register your models here.
admin.site.register(Artifact)
admin.site.register(Country)
admin.site.register(Museum)
admin.site.register(Game)