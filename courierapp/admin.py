from django.contrib import admin
from .models import Parcel,Totalcost

# Register your models here.

class ParcelModelAdmin(admin.ModelAdmin):
    list_display=['merchant_name','percel_type','order_place','weight','created_at']

admin.site.register(Parcel,ParcelModelAdmin)

class TotalcostModelAdmin(admin.ModelAdmin):
    list_display=['tcost','parcel']

admin.site.register(Totalcost,TotalcostModelAdmin)