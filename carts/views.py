from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from products.models import Product
from carts.models import Cart


@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_remove(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_edit(request, id, quantity):
    if request.is_ajax():
        cart = Cart.objects.get(id=id)
        if quantity > 0:
            cart.quantity = quantity
            cart.save()
        else:
            cart.delete()
        carts = Cart.objects.filter(user=request.user)
        context = {'carts': carts}
        result = render_to_string('carts/cart.html', context)
        return JsonResponse({'result': result})
