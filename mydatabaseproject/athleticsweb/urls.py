from django.contrib import admin
from django.urls import path
from athleticsweb import views

urlpatterns = [
	path('', views.index, name='index'),
]
