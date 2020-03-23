from django.shortcuts import render
from .models import Product
from django.db.models import Q

# Create your views here.
def all_products(request):
    products = Product.objects.filter(seller__icontains="AllinOne").distinct()

    return render(request, "products/products.html", {"products":products})