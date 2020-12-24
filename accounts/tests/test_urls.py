from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import Signup, UserPage


class TestUrls(SimpleTestCase):

    def test_signup(self):
        url = reverse('accounts:signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Signup)

    def test_userpage(self):
        url = reverse('accounts:userpage', args=['1']) #передаем pk=1
        self.assertEquals(resolve(url).func.view_class, UserPage)