from django.shortcuts import render
from django.http import HttpResponse
from .models import t1_houseinfo, t1_houseinfoalt

# Create your views here.

def home(request):
    # fetch all house information from the database
    houses = t1_houseinfo.objects.all()
    # render the home.html template with the house information
    return render(request, 'home.html', {'houses': houses})

def house_leaders(request):
    return render(request, 'house_leaders.html')

def facilities_schedule(request):
    return render(request, 'facilities_schedule.html')

def trophies_categories(request):
    return render(request, 'trophies_categories.html')

def query(request):
    return render(request, 'query.html')