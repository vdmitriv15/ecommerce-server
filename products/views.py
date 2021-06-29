from django.shortcuts import render

# Create your views here.


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
        'products': [
            {
                'name': 'black hood',
                'price': 40.80,
                'description': '........................................',
                'image': '/static/vendor/img/products/Adidas-hoodie.png'
            },
            {
                'name': 'blue jacket',
                'price': 230.47,
                'description': '........................................',
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'
            },
            {
                'name': 'brown cardigan',
                'price': 32.98,
                'description': '........................................',
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
            },
            {
                'name': 'black backpack',
                'price': 20.70,
                'description': '........................................',
                'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'
            },
            {
                'name': 'black shoes',
                'price': 123.97,
                'description': '........................................',
                'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'
            },
            {
                'name': 'sweatpants',
                'price': 31.52,
                'description': '........................................',
                'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
            },
        ]
    }
    return render(request, 'products/products.html', context)
