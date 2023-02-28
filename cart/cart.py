
class Cart():
    """
    A base Cart class, providing soem default behaviors that can be in herrited or overrided, as necessary.

    """
#initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:    #if session is unavail. it i will create new one 
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, feature, qty):
        # adding and updating the users cart session data 

        feature_id= feature.id 

        if feature_id not in self.cart:
            self.cart[feature_id] = {'price': feature.price, 'qty': int(qty)}

        self.session.modified = True

    def __len__(self): #getting cart data/ counting the item qty 
        
        return sum(item['qty'] for item in self.cart.values())  #how ever much the qty in each session sum the total and get data

