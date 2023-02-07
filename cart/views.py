from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .cart import Cart

def cart_summary(request): 
    return render(request, 'gifted/cart/summary.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        feature_id = int(request.POST.get('featureid'))
        feature = get_object_or_404(Feature, id= feature_id)
        cart.add(feature=feature)

