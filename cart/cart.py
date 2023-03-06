


class Cart():

#initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:    #if session is unavail. it i will create new one 
            cart = self.session['skey'] = {} #makes a new session
        self.cart = cart

 