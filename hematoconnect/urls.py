"""hematoconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hemo import views
from hemo.views import totalbloodview 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home',homeview.as_view(),name='home'),
    
    path('home',views.homeviews,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('donor',views.donor_register),
    path('donor_login',views.donor_login),
    path('bloodbank',views.bank_register),
    path('bank_login',views.bank_login),
    path('donate/<int:pk>',views.donate,name='donate'),
    path('donorhome',views.donorhome),
    path('donorhistory',views.donorhistory),
    # path('donorrequest',views.donorrequest),
    # path('requesthistory',views.requesthistory),
    path('recipientregister',views.recipient_register),
    path('recipient_login',views.recipient_login),
    path('recipienthome',views.recipienthome),
    path('recipientrequest/<int:pk>',views.recipientrequest,name='recipientrequest'),
    path('recipienthistory',views.recipienthistory),
    
    path('donorapproverequest/<int:pk>',views.donor_approvr_status,name='donorapproverequest'),
    path('donorrejectrequest/<int:pk>',views.donor_reject_status,name='donorrejectrequest'),
    path('deletedonor/<int:pk>',views.delete_donor,name='deletedonor'),

    path('recipientapproverequest/<int:pk>',views.recipient_approvr_status,name='recipientapproverequest'),
    path('recipientrejectrequest/<int:pk>',views.recipient_reject_status,name='recipientrejectrequest'),
    path('deletrecipient/<int:pk>',views.delete_recipient,name='deleterecipient'),
    
    path('bankhome',views.bankhome),
    path('bankdonor',views.bankdonor),
    path('bankdonation',views.bankdonation),
    path('bankrequest',views.bankrequest),
    path('bankdonor',views.bankdonor),
    path('bankrecipient',views.bankrecipient),
    path('banklist',views.banklist,name='banklist'),
    path('recipientbanklist',views.recipientbanklist,name='recipientbanklist'),
    path('hospitalbanklist',views.hospitalbanklist,name='hospitalbanklist'),

    path('hospitalhome',views.hospitalhome),
    path('hospitalregister',views.hospital_register),
    path('hospital_login',views.hospital_login),
    path('stock',views.stockupdate),
    path('addtocart',views.addcart,name='addtocart'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('summary',views.summary,name='summary'),
    path('changequantity',views.changequantity,name='changequantity'),
    path('totalbloodview',totalbloodview.as_view(),name='totalbloodview'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('paymentsuccess',views.paymentsuccess,name='paymentsuccess'),

    path('search',views.search,name='search'),
    path('rsearch',views.rsearch,name='rsearch'),

    path('logout',views.logout,name='logout'),
    path('recipientlogout',views.recipientlogout,name='recipientlogout'),
    path('banklogout',views.banklogout,name='banklogout'),

    path('donorprofile',views.donorprofile,name='donorprofile'),
    path('recipientprofile',views.recipientprofile,name='recipientprofile'),
    path('editdonor',views.donoreditprofile,name='editdonor'),
    path('editrecipient',views.recipienteditprofile,name='editrecipient'),

    # path('donordash',views.donordashboard),
    # path('hospitaldash',views.hospitaldash),
    # path('adminhome',views.adminhome,name='adminhome'),
    # path('admindonor',views.admindonor),
    # path('admindonation',views.admindonation),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)