
class Cart():
    """
    A base Cart class, providing soem default behaviors that can be in herrited or overrided, as necessary.

    """
#initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:    #if session is unavail. it i will create new 
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, feature):

    