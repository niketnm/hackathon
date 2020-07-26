from django.urls import path
from .views import product_list, add_to_cart

app_name='core'
urlpatterns = [
    path('', product_list, name='product-list'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart')

]