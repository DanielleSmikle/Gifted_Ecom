


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
    
    def __len__(self):              ##to get cart data/count qty
        return sum(item['qty'] for item in self.cart.values())



 