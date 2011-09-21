"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from scrape.parliment import views
from django.test.client import RequestFactory


class TestMakeRequest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_connection(self):
        """
        Tests that the function returns an empty list for a nonsense query.
        """
        request = self.factory.get('parliment/sparql/?query=dknfgklans')
        
        response = views.make_request(request)
        self.assertEqual(response, [])


    def test_json(self):
       """
       Tests the json is dumped correctly to the html.
       """