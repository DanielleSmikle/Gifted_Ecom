from django.test import TestCase
from django.contrib.auth.models import User

from gifted.models import Collection, Feature

class TestCollectionsModel(TestCase):

    def setUp(self):
        self.data1 = Collection.objects.create(name='django', slug= 'django')

    def test_collection_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Collection))


    def test_collection_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestFeatureModel(TestCase):
    def setUp(self):
        Collection.objects.create(name='django', slug='cashmere-musk')
        User.objects.create(username='admin')
        self.data1 = Feature.objects.create(collection_id=1, scent= 'cashmere musk', created_by_id=1,
                                            slug= 'cashmere-musk', price='10.05', image='cashmere')

def test_features_model_entry(self):
    data = self.data1
    self.assertTrue(isinstance(data, Feature))
    self.asssertEqual(str(data), 'cashmere-musk')