from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from gifted.models import Feature
from .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'gifted/cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        feature_id = int(request.POST.get('featureid'))
        feature_qty = int(request.POST.get('featureqty'))
        feature = get_object_or_404(Feature, id=feature_id)
        cart.add(feature=feature, qty= feature_qty)
        
        cartqty= cart.__len__()
        response = JsonResponse({'qty': cartqty})

        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        feature_id = int(request.POST.get('featureid'))
        cart.delete(feature=feature_id)
        response = JsonResponse({'Success': True})
        return response

def cart_update(request):
    cart= Cart(request)
    if request.POST.get('action')== 'post':
        feature_id = int(request.POST.get('featureid'))
        feature_qty= int(request.POST.get('featureqty'))
        cart.update(feature= feature_id, qty= feature_qty)

        response = JsonResponse({'Success': True})
        return response


