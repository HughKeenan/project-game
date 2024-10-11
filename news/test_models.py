from django.test import TestCase
from news.models import Thread, Response
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
        """Test the thread string representation."""
        self.assertEqual((str(self.model.body)),
            'This is a test thread')

    def test_thread_title(self):
        """Test the thread model title"""
        self.model.title = "This is a test title"
        self.model.save()
        self.assertEqual(self.model.title, "This is a test title")  

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
        """Test the response string representation."""
        self.assertEqual(
            (
                str(self.model.body)
            ),
            'This is a test response'
        )     

    def test_response_body(self):
        """Test the response model body"""
        self.model.body = "This is a test response"
        self.model.save()
        self.assertEqual(self.model.body, "This is a test response")       