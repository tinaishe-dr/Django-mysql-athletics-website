from django.shortcuts import render
from django.http import HttpResponse
from .models import Trophy, HouseInfo, HouseInfoAlt, HouseLeader, SportsCategory, CategoryIncharge, HIDinfo

# Create your views here.

def home(request):
    # fetch all house information from the database
    houses = HouseInfo.objects.all()
    house_alts = HouseInfoAlt.objects.all()
    return render(request, 'home.html', {'houses': houses, 'house_alts': house_alts})

def house_leaders(request):
    house_leaders = HouseLeader.objects.all()
    return render(request, 'house_leaders.html', {'house_leaders': house_leaders})

def trophies_categories(request):
    categories = SportsCategory.objects.all()
    incharge = CategoryIncharge.objects.all()
    trophies = Trophy.objects.all()
    hidinfos = HIDinfo.objects.all()
    trophiesinfo = HIDinfo.trophies.through.objects.all()
    return render(request, 'trophies_categories.html', {'trophies': trophies, 'categories': categories, 'incharge': incharge, 'hidinfos': hidinfos, 'trophiesinfo': trophiesinfo})

def facilities_schedule(request):
    return render(request, 'facilities_schedule.html')

def query(request):
    return render(request, 'query.html')