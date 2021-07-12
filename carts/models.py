from django.db import models
from users.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.product.name}'

    def amount(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        carts = Cart.objects.filter(user=self.user)
        return sum(cart.quantity for cart in carts)
