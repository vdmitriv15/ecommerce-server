from django.shortcuts import render
import os
import json

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Catalog',
        'header': 'GeekShop',
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    file = open(file_path, encoding='utf-8')
    context['products'] = json.load(file)
    return render(request, 'products/products.html', context)
