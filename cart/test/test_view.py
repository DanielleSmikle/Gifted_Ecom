from django.contrib.auth.models import User 
from django.test import TestCase
from django.urls import reverse 

from gifted.models import Collection, Feature

class TestCartView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Collection.objects.create(name='cashmere-musk', slug='cashmere-musk')
        Feature.objects.create(collection_id=1, scent='cashmere musk',
                                            slug='cashmere-musk', price='20.00', image='cashmere')
        Feature.objects.create(collection_id=1, scent='tabacco & bay leaf',
                                            slug='features', price='20.00', image='tabacco')
        Feature.objects.create(collection_id=1, scent='oak moss & amber',
                                            slug='oak-moss-amber', price='20.00', image='OakMoss')

        self.client.post(
            reverse('cart:cart_add'), {"featureid":1, "featureqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('cart:cart_add'), {"featureid":2, "featureqty": 2, "action": "post"}, xhr=True)
    
    def test_cart_url(self):
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)
    
    def test_cart_add(self):
        response= self.client.post(
            reverse('cart:cart_add'), {"featureid":3, "featureqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty':4})
        response = self.client.post(
            reverse('cart:cart_add'), {"featureid":2, "featureqty":1, "action": "post"}, xhr = True)
        self.assertEqual(response.json(), {'qty':3})
    
    def test_cart_delete(self):
        response = self.client.post(
            reverse('cart:cart_delete'), {"featureid":2, "action": "post"}, xhr = True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal':'20.0'})
    
    def test_cart_update(self):
        response= self.client.post(
            reverse('cart:cart_update'), {"featureid":2, "featureqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.0'})
        
        


    


        


