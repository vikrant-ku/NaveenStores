from django.db import models
from .customer import Customer


class Replace(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    image = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    reason = models.CharField(max_length=30)

    def __str__(self):
        return self.email


    def register(self):
        self.save()
