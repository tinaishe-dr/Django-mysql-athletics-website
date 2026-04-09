from django.db import models

# Create your models here.

class HouseInfo(models.Model):
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

class HouseInfoAlt(models.Model):
    HID_id = models.OneToOneField(HouseInfo, on_delete=models.CASCADE, db_column='HID_id', primary_key=True)
    HouseName = models.CharField(max_length=100)
    AltPhone = models.CharField(max_length=100, null=True, blank=True)
    AltEmail = models.EmailField(null=True, blank=True)

class HouseLeader(models.Model):
    HID_id = models.OneToOneField(HouseInfo, on_delete=models.CASCADE, db_column='HID_id', primary_key=True)
    HouseName = models.CharField(max_length=100)
    HCapID = models.CharField(max_length=100)
    HouseCaptain = models.CharField(max_length=100)
    HouseCaptainGrade = models.IntegerField()
    HVCapID = models.CharField(max_length=100)
    HouseViceCaptain = models.CharField(max_length=100)
    HouseViceCaptainGrade = models.IntegerField()
    CaptaincyTermStart = models.PositiveIntegerField()
    CaptaincyTermEnd = models.PositiveIntegerField()

class SportsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    CategoryId = models.CharField(max_length=100)
    CategoryName = models.CharField(max_length=100)
    GradeRangeJunior = models.CharField(max_length=100, null=True, blank=True)
    GradeRangeSenior = models.CharField(max_length=100, null=True, blank=True)

class CategoryIncharge(models.Model):
    id = models.AutoField(primary_key=True)
    InChargeGreen = models.CharField(max_length=100)
    InchargePink = models.CharField(max_length=100)
    InchargeBlue = models.CharField(max_length=100)
    InchargeGold = models.CharField(max_length=100)
    FacultyIncharge = models.CharField(max_length=100)
    ID_id = models.ForeignKey(SportsCategory, on_delete=models.CASCADE, db_column='ID_id')

class Trophy(models.Model):
    id = models.AutoField(primary_key=True)
    Trophy = models.CharField(max_length=100)

class HIDinfo(models.Model):
    id = models.AutoField(primary_key=True)
    HouseName = models.CharField(max_length=100)
    HouseNameAlt = models.CharField(max_length=100)
    trophies = models.ManyToManyField(Trophy, related_name='houses')