from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from gifted.models import Collection, Feature
from gifted.views import feature_all

@skip('demonstrating skipping')
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c =  Client()
        User.objects.create(username='admin')
        Collection.objects.create(name='cashmere-musk', slug='cashmere-musk')
        Feature.objects.create(collection_id=1, scent='cashmere musk',
                                            slug='cashmere-musk', price='10.05', image='cashmere')


    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_feature_detail_url(self):
        response = self.c.get(reverse('gifted:feature_detail', args=['cashmere-musk']))
        self.assertEqual(response.status_code, 200)

    def test_collection_detail_url(self):
        response = self.c.get(reverse('gifted:collection_list', args=['cashmere-musk']))
        self.assertEqual(response.status_code, 200)


    # def test_url_allowed_host(self):
    #     response = self.c.get('/', HTTP_HOST='')
    #     self.assertEqual(response.status_code, 400)
    #     response = self.c.get('/', HTTP_HOST='')
    #     self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request= HttpRequest()
        engine= import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = feature_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Gifted by GiGi </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
       

 
  
