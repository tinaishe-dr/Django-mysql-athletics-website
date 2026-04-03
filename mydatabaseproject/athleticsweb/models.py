from django.db import models

# Create your models here.

class t1_houseinfo(models.Model):
    id = models.AutoField(primary_key=True)
    HouseId = models.CharField(max_length=5)
    HouseEstd = models.IntegerField()
    HouseName = models.CharField(max_length=100)
    HouseNameAlt = models.CharField(max_length=100)
    HouseOffice = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Building = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.CharField(max_length=100)

class t1_houseinfoalt(models.Model):
    HID_id = models.AutoField(primary_key=True)
    HouseName = models.CharField(max_length=100)
    AltPhone = models.CharField(max_length=100)
    AltEmail = models.CharField(max_length=100)
    