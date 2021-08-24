from django.test import TestCase, Client
from .models import MappingUrl


class MappingUrlModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        MappingUrl.objects.create(originUrl="https://www.google.com", shortenString="12345678")

    def test_from_shortenString_get_originUrl(self):
        query_result = MappingUrl.objects.filter(shortenString="12345678")
        self.assertEqual(query_result[0].originUrl, "https://www.google.com")


class DataCreateTests(TestCase):
    client = Client()
    shortenedUrl = ''

    def testCreateData(self):
        response = self.client.post("/api/create_shorten_url", {"originUrl": "https://www.bing.com/"}, content_type='application/json')
        self.shortenedUrl = '/' + response.json()['shortenedUrl']
        response = self.client.get(self.shortenedUrl, follow=True)
        self.assertEqual(response.redirect_chain[0][0], "https://www.bing.com/")
        self.assertEqual(response.redirect_chain[0][1], 301)
        self.assertEqual(len(self.shortenedUrl), 9)
