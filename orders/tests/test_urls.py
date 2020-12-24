from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import OrderSummary, OrderDetail, OrderList


class TestUrls(SimpleTestCase):

    def test_order_detail(self):
        url = reverse('orders:order_detail', args=['20'])
        self.assertEquals(resolve(url).func.view_class, OrderDetail)