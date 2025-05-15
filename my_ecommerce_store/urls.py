from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from store.views import product_list  # Import the product list view
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore

urlpatterns = [  # Define main URL patterns first
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),  # Existing route for products
    path('', product_list, name='home'),  # This sets product_list as the homepage
]

# Append static URL handling AFTER defining urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)