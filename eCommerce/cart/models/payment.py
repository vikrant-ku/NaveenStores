from django.db import models
from datetime import datetime
from .customer import Customer

class Payment(models.Model):
    user = models.ForeignKey(Customer , on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.razorpay_order_id