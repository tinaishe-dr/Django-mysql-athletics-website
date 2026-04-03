from django.shortcuts import render
from django.http import HttpResponse
from .models import t1_houseinfo, t1_houseinfoalt

# Create your views here.

def index(request):
    # fetch all house information from the database
    houses = t1_houseinfo.objects.all()
    # render the index.html template with the house information
    return render(request, 'home.html', {'houses': houses})