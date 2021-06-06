from django.db import models
from .customer import Customer
from .product import Product
from .payment import Payment
from datetime import datetime

STATUS_CHOICES =(
    ("Ordered", "Ordered"),
    ("On The Way", "ontheway"),
    ("Shipped", "Shipped"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
    ("Replace", "Replace"),
  )
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='' )
    color = models.CharField(max_length=20, default="")
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    address = models.TextField(default="")
    city = models.CharField(max_length=20, default='')
    zip_code = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=15, default='')
    order_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES , default="Ordered")
    order_delevered_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def register(self):
        self.save()


    @staticmethod
    def get_orders_by_customer(customer_id):
        try:
            return Orders.objects.filter(customer_id=customer_id).order_by('-order_date')
        except:
            return False

    @staticmethod
    def get_order_by_id(id):
        try:
            return Orders.objects.get(order_id= id)
        except:
            return False
