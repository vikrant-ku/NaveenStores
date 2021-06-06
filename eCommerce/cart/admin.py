from django.contrib import admin
from .models.category import Category
from .models.product import Product, FbLive
from .models.customer import Customer, Cart
from .models.orders import Orders
from .models.contact_us import Contact
from .models.subscribers import Subscriber
from .models.billing import Billing
from .models.cancle_order import Cancel_order
from .models.replace import Replace
from .models.payment import Payment


# Register your models here.
class ProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'lable', 'type')
    list_filter = ('category', 'subcategory', 'type', 'lable')
    search_fields = ['name', 'sr_no','category__Name', 'subcategory', 'type', 'lable']
    list_editable = ('lable', 'type')

class Payment_Admin(admin.ModelAdmin):
    search_fields = ['user', 'razorpay_order_id',]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','name', 'email', 'order_date', 'status', 'order_delevered_date')
    search_fields = ['order_id','name', 'email',  'status']
    list_editable = ( 'status',)

class CancelAdmin(admin.ModelAdmin):
    list_display = ('customer', 'phone', 'email', 'reason')

class FBLiveAdmin(admin.ModelAdmin):
    raw_id_fields = ("prodsr_no",)

admin.site.register(Category)
admin.site.register(Product, ProdAdmin)
admin.site.register(FbLive, FBLiveAdmin)
admin.site.register(Customer)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Cart)
admin.site.register(Payment,Payment_Admin)
admin.site.register(Subscriber)
admin.site.register(Replace)
admin.site.register(Cancel_order, CancelAdmin)
admin.site.register(Billing)
admin.site.register(Contact, ContactAdmin)

