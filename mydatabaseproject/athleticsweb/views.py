from django.shortcuts import render
from django.http import HttpResponse
from .models import t1_houseinfo, t1_houseinfoalt, t1_houseleaders

# Create your views here.

def home(request):
    # fetch all house information from the database
    houses = t1_houseinfo.objects.all()
    house_alts = t1_houseinfoalt.objects.all()
    return render(request, 'home.html', {'houses': houses, 'house_alts': house_alts})

def house_leaders(request):
    house_leaders = t1_houseleaders.objects.all()
    return render(request, 'house_leaders.html', {'house_leaders': house_leaders})

def facilities_schedule(request):
    return render(request, 'facilities_schedule.html')

def trophies_categories(request):
    return render(request, 'trophies_categories.html')

def query(request):
    return render(request, 'query.html')