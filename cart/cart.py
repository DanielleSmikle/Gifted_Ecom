from decimal import Decimal

from gifted.models import Feature


class Cart(): #initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:#if session is unavail. it i will create new one 
            cart = self.session['skey'] ={} #makes a new session
        self.cart = cart

    def add(self, feature, qty):
        feature_id = str(d)

        if feature_id in self.cart:
            self.cart[feature_id]['qty'] = qty
        else:
            self.cart[feature_id] = {'price': str(feature.price), 'qty': qty}

        self.save()
    
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

    def __len__(self): ##to get cart data/count qty
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, feature):  ##deletes item from session data
        feature_id= str(feature)
      
        if feature_id in self.cart:
            print(feature_id)
            del self.cart[feature_id]
        
        self.save()

    def update(self, feature, qty):    ##update session data values
        feature_id = str(feature)
        qty = qty

        if feature_id  in self.cart:
            self.cart[feature_id]['qty'] = qty

        self.save()

    def save(self):
        self.session.modified = True
