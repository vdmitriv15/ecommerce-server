from django.urls import path

from carts.views import cart_add

app_name = 'carts'

urlpatterns = [
    path('add/<int:product_id>', cart_add, name='cart_add')
]
