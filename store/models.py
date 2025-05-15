from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ✅ Product Model (Optimized for Performance)
class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Indexed for fast searches
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Ensure stock is never negative
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Auto timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    class Meta:
        indexes = [
            models.Index(fields=["name"]),  # Index for quick lookups
            models.Index(fields=["price"]),  # Useful for price-based filtering
            models.Index(fields=["created_at"]),  # Optimize historical queries
        ]

    def update_stock(self, amount):
        """Ensures stock doesn't become negative."""
        if self.stock - amount >= 0:
            self.stock -= amount
            self.save()
        else:
            raise ValueError("Insufficient stock")

    def __str__(self):
        return self.name

# ✅ Cart Model (Optimized with User Tracking)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow guest carts
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ["user", "product"]  # Prevent duplicate product entries per user

    def remove_item(self):
        """Safely reduce item quantity or remove from cart."""
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

# ✅ Order Model (Optimized for Historical Queries)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Preserve orders if user is deleted
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Track order time
    updated_at = models.DateTimeField(auto_now=True)  # Track status updates

    class Meta:
        ordering = ["-created_at"]  # Show recent orders first
        indexes = [
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"Order {self.id} - {self.user.username if self.user else 'Guest'}"

# ✅ Order Item Model (Tracking Order Details)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"