from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from base.models import *
from base.urls import urlpatterns


class UserUrlsTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user('test', 'test@email.com', 'testtest')
        topic_instance = Topic.objects.create(name="Papa")
        room_instance = Room.objects.create(topic=topic_instance, host=self.user, name='Algebra')
        Message.objects.create(user=self.user, room=room_instance, body='Some text')
        RoomCount.objects.create(topic=topic_instance)

    def test_profile(self):
        resp = self.client.get(reverse('user-profile', args=(1,)), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_room_page(self):
        resp = self.client.get(reverse('room-page', args=(1,)), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_update_room_logged(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('update-room', args=(1,)), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_delete_room_logged(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('delete-room', args=(1,)), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_delete_message_logged(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('delete-message', args=(1,)), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_redirect_if_not_logged_in_create_room(self):
        resp = self.client.get(reverse('create-room'))
        self.assertRedirects(resp, '/login/?next=/create-room')



    # def test_all_urls(self):
    #     for pattern in urlpatterns:
    #         if 'pk' in str(pattern):
    #             print(pattern.name)
    #             response = self.client.get(reverse(pattern.name, args=(1,)), follow=True)
    #             self.assertEqual(response.status_code, 200)
    #         else:
    #             response = self.client.get(f'/{pattern.pattern}', follow=True)
    #             self.assertEqual(response.status_code, 200)
