from django.test import SimpleTestCase
from django.urls import resolve, reverse
from base.views import home


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

