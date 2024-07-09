from django.db import models

# model for product

class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHICES=((LIVE,'LIVE'),(DELETE,'DELETE'))   #for recycle_bin purpos
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)   #for sessonal priority items
    delete_status=models.IntegerField(choices=DELETE_CHICES,default=LIVE)
    created_at=models.DateTimeField(auto_now=True) #for delete and updated time intication
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title