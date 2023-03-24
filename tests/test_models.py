from django.test import TestCase

from gifted.models import Collection, Feature

class TestCollectionsModel(TestCase):

    def setUp(self):
        self.data1 = Collection.objects.create(name='django', slug= 'django')

    def test_collection_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Collection))