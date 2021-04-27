from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Parcel,Totalcost
from .forms import ParcelForm


# Create your views here.
# def home(request):
#     parcel=Parcel.objects.all()
#     return render (request,'index.html',{"parcel":parcel})

# def add_parcel_save(request):
#     if request.method=="POST":
#         merchant_name=request.POST.get("merchant_name")
#         percel_type=request.POST.get("percel_type")
#         merchant_id=request.POST.get("merchant_id")
#         order_place=request.POST.get("order_place")
#         weight=request.POST.get("weight")
#         p=Parcel(merchant_name=merchant_name,percel_type=percel_type,merchant_id=merchant_id,order_place=order_place,weight=weight)
#         p.save()
#         messages.success(request,'Congratulation !! Parcel Create Successfully')
#     else:
#         return render (request,'index.html')

class ParcelView(View):
    def get(self,request):
        form=ParcelForm()
        show=Parcel.objects.all()
        # waa=Parcel.objects.filter(weight='wa')
        # wbb=Parcel.objects.filter(weight='wb')
        # print(waa)
        # in_side=Parcel.objects.filter(order_place='i_d')
        # print("inside dhaka",in_side)
        # cost=0
        # inside_dhaka=Parcel.objects.filter(order_place='ID')
        # cost=0
        # if Parcel.objects.filter(order_place=inside).filter(weight=waa):
        #     cost=cost+60
        #     print(cost)
        # if Parcel.objects.filter(order_place='ID').filter(weight='wb'):
        #     cost=70
        #     print(cost)
        cost=0
        a=Parcel.objects.filter(order_place='ID', weight='wa').order_by('id').first()
        b=Parcel.objects.filter(order_place='ID', weight='wb').order_by('id').first()
        print(a)
        # place = Parcel.objects.get(name='kansas').values('id')[0]['id']

        if Parcel.objects.filter(order_place='ID', weight='wa'):
            cost=60
            p=Totalcost(tcost=cost,parcel=a)
        elif Parcel.objects.filter(order_place='ID', weight='wb'):
            cost=70
            p=Totalcost(tcost=cost,parcel=b)
        p.save()
        return render(request, 'parcel.html',{'form':form,'show':show})
    def post(self,request):
        form=ParcelForm(request.POST)
        if form.is_valid():
            merchant_name=form.cleaned_data['merchant_name']
            percel_type=form.cleaned_data['percel_type']
            merchant_id=form.cleaned_data['merchant_id']
            order_place=form.cleaned_data['order_place']
            weight=form.cleaned_data['weight']
            r=Parcel(merchant_name=merchant_name,percel_type=percel_type,merchant_id=merchant_id,order_place=order_place,weight=weight)
            r.save()
            messages.success(request,'Congratulation !! Parcel Create Successfully')
            return redirect('parcel')
        return render(request, 'parcel.html',{'form':form})
       

# def showcost(request):
#         cost=0
#         cost2=0
#         cost3=0
#         # abc=Parcel.objects.filter(order_place='ID', weight='wa')
#         # print(abc)
#         # ab=Parcel.objects.filter(order_place='ID', weight='wb')
#         # print(ab)
#         if Parcel.objects.filter(order_place='ID', weight='wa'):
#             cost=60
#             print(cost)
#             return cost
#         elif Parcel.objects.filter(order_place='ID', weight='wb'):
#             cost=70
#             print(cost)
#             return cost
#         p=Totalcost(tcost=cost)
#         p.save()
# class ShowParcel(View):
#     def get(self,request):
#         show=Parcel.objects.all()
#         return render(request, 'parcel.html',{'show':show})
# def showparcel(request):
#     show=Parcel.objects.all()
#     return render(request, 'parcel.html',{'show':show})
       
