from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from base.models import Room, Message, Topic
from base.views import home
from base.urls import urlpatterns
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)


class UserUrlsTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="lion", email="lion@mail.ru")
        User.objects.create(username="cat", email="meow@mail.ru")
        topic_instance = Topic.objects.create(name="Papa")
        Room.objects.create(topic=topic_instance, host=user1, name='Algebra')

    def test_profile(self):
        response = self.client.get(reverse('user-profile', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_room(self):
        response = self.client.get(reverse('update-room', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        for pattern in urlpatterns:
            # print(pattern.pattern)
            response = self.client.get('', follow=True)

            self.assertEqual(response.status_code, 200)
