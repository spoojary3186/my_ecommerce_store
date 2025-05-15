from django.contrib import admin
from django.urls import path, include
from store.views import product_list  # Import the product list view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),  # Existing route for products
    path('', product_list, name='home'),  #  This sets product_list as the homepage
]