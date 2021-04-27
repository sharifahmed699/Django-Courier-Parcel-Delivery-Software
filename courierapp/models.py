from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parcel(models.Model):
    WEIGHT=(
        ('wa','500 gm to 2 kg'),
        ('wb','3 kg'),
        ('wc','4 kg'),
        ('wd','5 kg'),
    )
    PERCEL_TYPE=(
        ('fragile','Fragile'),
        ('liquid','Liquid')
    )
    ORDER_PLACE=(
        ('ID','Inside of Dhaka'),
        ('DD','Division of Dhaka'),
        ('OD','Outside of Dhaka')
    )
    
    merchant_name=models.ForeignKey(User,on_delete=models.CASCADE)
    percel_type=models.CharField(choices=PERCEL_TYPE,max_length=50)
    merchant_id=models.CharField(max_length=50)
    order_place=models.CharField(choices=ORDER_PLACE,max_length=50)
    weight=models.CharField(choices=WEIGHT,max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_order_place_display()
    
    def __str__(self):
        return self.get_weight_display()

    # def showcost(self):
    #     cost=0
    #     cost2=0
    #     cost3=0
    #     # abc=Parcel.objects.filter(order_place='ID', weight='wa')
    #     # print(abc)
    #     # ab=Parcel.objects.filter(order_place='ID', weight='wb')
    #     # print(ab)
    #     if Parcel.objects.filter(order_place='ID', weight='wa'):
    #         cost=60
    #         print(cost)
    #         # return cost
    #     elif Parcel.objects.filter(order_place='ID', weight='wb'):
    #         cost=70
    #         print(cost)
    #     return cost
        # in_dhaka=Parcel.objects.filter(order_place='ID')
        # a=in_dhaka
        # div_dhaka=Parcel.objects.filter(order_place='DD')
        # out_dhaka=Parcel.objects.filter(order_place='OD')
        # weighta=Parcel.objects.filter(weight='wa')
        # weightb=Parcel.objects.filter(weight='wb')
        # weightc=Parcel.objects.filter(weight='wc')
        # weightd=Parcel.objects.filter(weight='wd')
        # if in_dhaka == 'wa':
        #     cost=60
        #     print(cost)
        #     return cost
        # elif in_dhaka == 'wb':
        #     cost=70
        #         # print(cost)
        #     return cost
        # elif in_dhaka == 'wc':
        #     cost=80
        #         # print(cost)
        #     return cost
        # elif in_dhaka == 'wd':
        #     cost=90
        #         # print(cost)
        #         # return cost
        #     return cost


            
    # def showcost(self):
    #     cost=0
    #     if Parcel.objects.filter(order_place='i_d'):
    #         if Parcel.objects.filter(weight='wa'):
    #             cost=60
    #             return cost
    #         else:
    #             cost=0
    #             return cost
            




class Totalcost(models.Model):
    tcost=models.FloatField()
    parcel=models.ForeignKey(Parcel, on_delete=models.CASCADE)
