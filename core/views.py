from django.shortcuts import render
from .models import Item

def product_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product_list.html', context)

def checkout(request): 
    return render(request, 'checkout.html', context)

def cart(request):
    return render(request, 'cart.html', context)
