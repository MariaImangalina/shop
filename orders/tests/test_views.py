from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login

from orders.views import OrderSummary, OrderDetail, OrderList
from orders.models import OrderGood, Order


User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser1', password='12345')
        self.client.login(username='testuser1', password='12345')
        self.detail_url = reverse('orders:order_detail', args=['1'])
        self.list_url = reverse('orders:all')
        print(self.list_url)


    def test_order_list(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        