from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from gifted.models import Collection, Feature
from gifted.views import feature_all

# @skip('demonstrating skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
# 

class TestViewResponses(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
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

    def test_homepage_html(self):
        request= HttpRequest()
        response = feature_all(request)
        html = response.content.decode('utf8')
        print(html)

    def test_view_function(self): 
        request= self.factory.get()
