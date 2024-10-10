from django.test import TestCase
from .models import Thread
from django.contrib.auth.models import User


# class TestThread(TestCase):

#     self.user = User.objects.create(
#         username = 'JohnD',
#     )

#     self.model = Thread.objects.create(
#         title='Test thread',
#         slug='test-thread',
#         poster= self.user, created = User.objects.get_or_create(username="JohnD"),
#         body='This is a test thread',
#         posted_on='10/10/2024',
#         visible=0,
#     )    

#     def test_model_is_valid(self):
#         self.assertEqual(self.model.has_body(), True)


class TestThread(TestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='JohnD')

        self.model = Thread.objects.create(
            title='Test thread',
            slug='test-thread',
            poster=self.user,
            body='This is a test thread',
            posted_on='2024-10-10',
            visible=0,
        )

    def test_model_is_valid(self):
        self.assertTrue(self.model.has_body())