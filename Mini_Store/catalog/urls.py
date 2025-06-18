from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views
app_name = "Catalog"
urlpatterns = [
    path("",views.catalog_product,name="list_product"),
    path("product/",views.product_list,name="product"),
    
]