from django.db import models
from .customer import Customer
from .orders import Orders



class Cancel_order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    refund_id = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    reason = models.CharField(max_length=30)

    def __str__(self):
        return self.name




