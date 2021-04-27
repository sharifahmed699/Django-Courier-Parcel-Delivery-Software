from django.urls import path
from courierapp import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.ParcelView.as_view(),name="parcel"),
    # path('',views.showparcel,name="show"),
    
    
]
