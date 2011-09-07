"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from scrape.tweet import views
from django.test.client import RequestFactory


class TestTweetView(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_connection(self):
        """
        Tests that the function returns a 200 status code.
        """
        request = self.factory.get('tweets/pvddr/10')
        
        response = views.tweet_view(request, 'pvddr', '10')
        self.assertEqual(response.status_code, 200)


    def test_get_tweets(self):
        """
        Tests ability to get tweets.
        """
        
        items = views.get_tweets('WayneViers', '9')
        self.assertEqual(len(items), 9)
        self.assertEqual(items[0], "tweets")
        self.assertEqual(items[8], "this")
        
        
        #Testing to see if an empty list is returned for a bad request
        items = views.get_tweets('dfsdfsdfevbbrnfghnejd', '10')
        self.assertEqual(len(items), 0)
        
        
        items = views.get_tweets('WayneViers', '1002330')
	self.assertEqual(len(items), 0)
        