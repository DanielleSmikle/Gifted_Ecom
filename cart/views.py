from django.shortcuts import render

def cart_summary(request): 
    return render(request, 'gigi/cart/summary.html')
