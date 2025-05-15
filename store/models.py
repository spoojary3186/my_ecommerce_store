from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# ✅ Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

# ✅ Cart Model
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def remove_item(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()  # Remove the item completely if quantity = 1

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

# ✅ Order Model (Ensuring Order History Works)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null for guest checkout
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, blank=True)  # Ensures timestamps are stored

    def __str__(self):
        return f"Order {self.id} - {self.user.username if self.user else 'Guest'}"

# ✅ Order Item Model (Tracks Products in Each Order)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"
    

