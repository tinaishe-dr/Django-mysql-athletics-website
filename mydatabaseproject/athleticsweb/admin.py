from django.contrib import admin
from .models import HIDinfo, HouseInfo, HouseInfoAlt, HouseLeader, PracticeSchedule, SportsCategory, CategoryIncharge, SportsFacility, Trophy

# Register your models here.
admin.site.register(HouseInfo)
admin.site.register(HouseInfoAlt)
admin.site.register(HouseLeader)
admin.site.register(SportsCategory)
admin.site.register(CategoryIncharge)
admin.site.register(Trophy)
admin.site.register(HIDinfo)
admin.site.register(SportsFacility)
admin.site.register(PracticeSchedule)