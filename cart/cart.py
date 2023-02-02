

class Cart():
    """
    A base Cart class, providing soem default behaviors that can be in herrited or overrided, as necessary.

    """
#initialize method, function will be ran right away with new obj created 
    def __init__(self, request):
       self.session= request.session
       cart = self.session.get('skey')