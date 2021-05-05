# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Customer
from .models import Item
from .models import Order
from .models import ItemList


admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(ItemList)
# Register your models here.
