from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def test_list_url(self):
        assert 1 == 2