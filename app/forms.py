from django import forms
from django.forms import ModelForm
from .models import Customer
from .models import ItemList
from .models import Order
from .models import Item
from .models import User
from .models import Payment


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'


class CustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = '__all__'


class ItemForm(forms.Form):
    class Meta:
        model = Item
        fields = '__all__'


class PaymentForm(forms.Form):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = '__all__'


class ItemListForm(forms.Form):
    class Meta:
        model = ItemList
        fields = '__all__'
