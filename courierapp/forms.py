from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model=Parcel
        fields=['merchant_name','percel_type','merchant_id','order_place','weight']
        widgets={
            'merchant_name':forms.Select(attrs={'class':'form-control'}),
            'percel_type':forms.Select(attrs={'class':'form-control'}),
            'merchant_id':forms.TextInput(attrs={'class':'form-control'}),
            'order_place':forms.Select(attrs={'class':'form-control'}),
            'weight':forms.Select(attrs={'class':'form-control'})
        }