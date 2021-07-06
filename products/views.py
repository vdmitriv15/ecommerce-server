from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Catalog',
        'header': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
