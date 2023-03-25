from unittest import skip

from django.test import TestCase
from django.contrib.auth.models import User

from gifted.models import Collection, Feature
from django.urls import reverse
from django.test import Client


# @skip('demonstrating skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
# 

class TestViewResponses(TestCase):
    def setUp(self):
        self.c =  Client()

    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_feature_detail_url(self):
        response = self.c.get(reverse)

