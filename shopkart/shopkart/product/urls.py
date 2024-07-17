from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('products_list',views.list_product,name='list_products'),
    path('product_details/<pk>',views.product_details,name='product_details'),
]