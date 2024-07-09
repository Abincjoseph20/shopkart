from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHICES = ((LIVE, 'LIVE'), (DELETE, 'DELETE'))  # for recycle_bin purpos
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone = models.CharField(max_length=10)
    priority = models.IntegerField(default=0)  # for sessonal priority items
    delete_status = models.IntegerField(choices=DELETE_CHICES, default=LIVE)
    created_at = models.DateTimeField(auto_now=True)  # for delete and updated time intication
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name