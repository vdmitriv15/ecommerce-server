from django.urls import path

from carts.views import cart_add, cart_remove, cart_edit

app_name = 'carts'

urlpatterns = [
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:id>', cart_remove, name='cart_remove'),
    path('edit/<int:id>/<int:quantity>/', cart_edit, name='cart_edit'),

]
