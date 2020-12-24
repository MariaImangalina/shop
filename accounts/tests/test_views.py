from django.test import TestCase, Client
from django.urls import reverse

from accounts.views import Signup, UserPage
from accounts.models import UserProfile

import json

class TestViews(TestCase):

    def setUp(self):  #начальные условия, запускаются перед каждым тестом
        self.client = Client()
        self.signup_url = reverse('accounts:signup')
        self.detail_url = reverse('accounts:userpage', args=['3'])

    def test_signup(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')


    def test_userpage(self):
        response = self.client.get(self.detail_url)

        print(response)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/user_detail.html')