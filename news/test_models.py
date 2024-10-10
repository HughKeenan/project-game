from django.test import TestCase
from .models import Thread, Response
from django.contrib.auth.models import User


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
        

    def test_thread_str(self):
        """Test the sales string representation."""
        self.assertEqual(
            (
                str(self.model.body)
            ),
            'This is a test thread'
        )

class TestResponse(TestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='JohnD')
        self.thread, created = Thread.objects.get_or_create(
            title='Test thread',
            slug='test-thread',
            poster=self.user,
            body='This is a test thread',
            posted_on='2024-10-10',
            visible=0,)

        self.model = Response.objects.create(
            poster=self.user,
            thread = self.thread,
            body='This is a test response',
            posted_on='2024-10-10',
            visible=0,
        )
        

    def test_response_str(self):
        """Test the sales string representation."""
        self.assertEqual(
            (
                str(self.model.body)
            ),
            'This is a test response'
        )        