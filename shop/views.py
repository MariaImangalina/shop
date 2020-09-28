from django.views import generic
from django.contrib.auth import get_user_model

User = get_user_model

class HomePage(generic.TemplateView):
    template_name = 'index.html'

class DeliveryInfoPage(generic.TemplateView):
    template_name =  'delivery_payment.html'