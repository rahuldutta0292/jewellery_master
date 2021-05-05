# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin_view, name="signin"),
    path('signout/', views.signout_view, name="signout"),
    path('order/', views.order, name="order"),
    path('PlaceOrder/', views.placeorder, name="placeorder"),
    path('order/add/', views.addorder, name="addorder"),
    path('customer/', views.customer, name="customer"),
    path('get/customer/validate/contact', views.checkcontact, name="checkcontact"),
    path('customer/add/', views.addcustomer, name="addcustomer"),
    path('customer/<int:customer_id>/change/', views.changecustomer, name="changecustomer"),
    # path('CreatePUC/<int:file_id>/add/', views.createpuc, name="create_puc"),
    # path('FileList/', views.filelist, name="file_list"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
