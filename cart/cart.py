from gifted.models import Feature
from decimal import Decimal



class Cart():

#initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:    #if session is unavail. it i will create new one 
            cart = self.session['skey'] = {} #makes a new session
        self.cart = cart

    def add(self, feature, qty):
        feature_id = feature.id

        if feature_id not in self.cart:
            self.cart[feature_id] = {'price': str(feature.price), 'qty':int(qty)}

        self.session.modified = True
    
    def __iter__(self): 
        feature_ids = self.cart.keys()
        features = Feature.features.filter(id__in=feature_ids)
        cart = self.cart.copy()

        for feature in features:
            cart[str(feature.id)]['feature']= feature
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    
    
    def __len__(self):              ##to get cart data/count qty
        return sum(item['qty'] for item in self.cart.values())



 