from django.db import models
from customers.models import Customer
from product.models import Product
# Create your models here.


class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHICES = ((LIVE, 'LIVE'), (DELETE, 'DELETE'))  # for recycle_bin purpos

    CART_STAGE=0   #for order status
    ORDER_CONFORMED=1
    ORDER_PROCCED=2
    ORDER_DELIVERD=3
    ORDER_REJECTED=4
    STATUS_CHICE=((ORDER_PROCCED,'ORDER_PROCCED'),
                  (ORDER_DELIVERD,'ORDER_DELIVERD'),
                  (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status = models.IntegerField(choices=STATUS_CHICE,default=CART_STAGE)

    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')# access from customer model
    delete_status = models.IntegerField(choices=DELETE_CHICES, default=LIVE)
    created_at = models.DateTimeField(auto_now=True)  # for delete and updated time intication
    updated_at = models.DateTimeField(auto_now=True)


class OrderedItem(models.Model): #for add item to cart usage
    product = models.ForeignKey(Product,related_name='added_cart',on_delete=models.SET_NULL,null=True,) #access from Products model
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
