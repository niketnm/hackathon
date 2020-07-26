from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.shortcuts import redirect
from django.utils import timezone

def product_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product_list.html', context)

def checkout(request): 
    return render(request, 'checkout.html', context)

def cart(request):
    return render(request, 'cart.html', context)

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        Order.items.add(order_item)
    return redirect("http://localhost:8000/product")
    

