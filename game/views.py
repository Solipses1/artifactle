from django.shortcuts import render
from datetime import date
from .models import Museum, Artifact, Country, Game

# Create your views here.
def index(request):
    current_date = date.today()
    try:
        game = Game.objects.get(date=current_date)
    except Game.DoesNotExist:
        game = Game.objects.latest("id")
    game_date = game.date
    countries = Country.objects.all()
    return render(request, "game/index.html", {
        "date": game_date,
        "countries": countries,
        "game": game,
        "artifact_1": game.round_1,
        "artifact_2": game.round_2,
        "artifact_3": game.round_3,
    })

def register(request):
    return render(request, "game/register.html")

def login(request):
    return render(request, "game/login.html")

def profile(request, user):
    return render(request, "game/profile.html")

def info(request):
    return render(request, "game/info.html")
