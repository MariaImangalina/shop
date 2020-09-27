from django import forms
from .models import Order, DELIVERY_TYPE, PICKUPS
from django.contrib.auth import get_user_model

User = get_user_model()



class CheckoutForm(forms.ModelForm):
    delivery_options = forms.CharField(max_length=50, widget=forms.RadioSelect(choices=DELIVERY_TYPE))
    pickup_point = forms.CharField(max_length=50, widget=forms.RadioSelect(choices=PICKUPS))
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ('phone', 'email', 'delivery_options', 'address', 'pickup_point')
