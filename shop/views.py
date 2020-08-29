from django.views import generic
from django.contrib.auth import get_user_model

User = get_user_model

class HomePage(generic.TemplateView):
    template_name = 'index.html'