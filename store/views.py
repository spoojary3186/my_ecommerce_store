from django.shortcuts import render, redirect
from .models import Product, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm

# ✅ Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# ✅ Add to Cart
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

# ✅ Remove from Cart
def remove_from_cart(request, product_id):
    cart_item = Cart.objects.filter(product_id=product_id).first()
    if cart_item:
        cart_item.remove_item()
    return redirect('cart_view')

# ✅ View Cart
@login_required
def cart_view(request):
    cart_items = Cart.objects.all()
    return render(request, 'store/cart.html', {'cart_items': cart_items})

# ✅ Checkout (Ensuring Order Saves Properly)
@login_required
def checkout(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        email = request.POST.get("email")

        # ✅ Create an order linked to the logged-in user
        order = Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            email=email,
            total_price=total_price
        )

        # ✅ Store order items
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        # ✅ Clear cart after checkout
        Cart.objects.all().delete()

        return redirect("checkout_success")

    return render(request, "store/checkout.html", {"cart_items": cart_items, "total_price": total_price})

# ✅ Checkout Success Page
def checkout_success(request):
    return render(request, 'store/checkout_success.html')

# ✅ Signup Function
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log in after registration
            return redirect('product_list')
    else:
        form = SignupForm()
    
    return render(request, 'store/signup.html', {'form': form})

# ✅ Login Function
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, "store/login.html", {"error": "Invalid credentials"})

    return render(request, "store/login.html")

# ✅ Logout Function
def user_logout(request):
    logout(request)
    return redirect('product_list')

# ✅ Order History (Fetching Orders Properly)
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})