from django.contrib import admin
from django.urls import path
from athleticsweb import views

urlpatterns = [
	path('', views.home, name='home'),
    path('house_leaders/', views.house_leaders, name='house_leaders'),
    path('facilities_schedule/', views.facilities_schedule, name='facilities_schedule'),
	path('trophies_categories/', views.trophies_categories, name='trophies_categories'),
	path('query/', views.query, name='query'),
]
