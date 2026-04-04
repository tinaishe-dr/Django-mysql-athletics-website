from django.db import models

# Create your models here.

class t1_houseinfo(models.Model):
    id = models.AutoField(primary_key=True)
    HouseId = models.IntegerField()
    HouseEstd = models.IntegerField()
    HouseName = models.CharField(max_length=100)
    HouseNameAlt = models.CharField(max_length=100)
    HouseOffice = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Building = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField()

class t1_houseinfoalt(models.Model):
    HID_id = models.OneToOneField(t1_houseinfo, on_delete=models.CASCADE, db_column='HID_id', primary_key=True)
    HouseName = models.CharField(max_length=100)
    AltPhone = models.CharField(max_length=100, null=True, blank=True)
    AltEmail = models.EmailField(null=True, blank=True)
    