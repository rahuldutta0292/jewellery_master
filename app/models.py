# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=200, null=True)
    user_control = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    contact = models.BigIntegerField(null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    pan = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.customer_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    order_amount = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    tax_amount = models.IntegerField(null=True)
    order_details = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.order_details:
            return self.order_details
        else:
            return self.customer


class ItemList(models.Model):
    item_name = models.CharField(max_length=50)
    item_weight = models.IntegerField(null=True, blank=True)
    item_availability = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.item_name


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True)
    weight = models.IntegerField(null=True)
    rate_per_gram = models.IntegerField(null=True)
    charge_per_gram = models.IntegerField(null=True)
    making_charge = models.IntegerField(null=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.item_name


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(null=True)
    remarks = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.amount


# Create your models here.`
