from django.views import  View
from django.shortcuts import render , redirect,get_object_or_404
from cart.models.customer import Customer
from cart.models.orders import Orders
from cart.models.cancle_order import Cancel_order
from datetime import datetime
from cart.models.payment import Payment
from django.contrib import messages
from cart.models.product import Product
from .pages import card_len

import razorpay
from django.conf import settings
keyid = settings.RAZORPAY_KEYID
keysecret = settings.RAZORPAY_KEYSECRET
razorpay_client = razorpay.Client(auth=(keyid, keysecret))
    
class Order_cancel(View):
    def get(self, request, id):
        len_cart= card_len(request)

        try:
            user = request.session.get('customer_id')
        except:
            user = False
        if user:

            order = Orders.get_order_by_id(id)
            if order:
                if order.status == 'Ordered':
                    cart_prod = {

                        'len': len_cart,
                        'order': order
                    }
                    return render(request, 'cancellation_form.html',cart_prod)
                else:
                    return redirect('profile')
            else:
                return redirect('profile')
        else:
            return redirect('home')

    def post(self, request):
        customer = request.session.get('customer_id')
        order_id = request.POST.get('order_id')
        name =  request.POST.get('name')
        phone =  request.POST.get('phone')
        email =  request.POST.get('email')
        reason =  request.POST.get('reason')
        order = Orders.get_order_by_id(int(order_id))
        prod = get_object_or_404(Product, id=order.product.id)

        #Refund
        payment = Payment.objects.get(pk=order.payment.pk)
        refund = razorpay_client.payment.refund(payment.razorpay_payment_id,order.price*100)
        #save cancel order
        cancel = Cancel_order(customer=Customer(id=customer),refund_id=refund.id,
                              order_id=order, name=name, phone=phone, email=email, reason=reason)
        cancel.save()

        order.status = "Cancelled"
        order.order_delevered_date = datetime.now()
        order.register()

        # cahange product stock
        prod.stock= order.quantity+prod.stock
        prod.save()

        error_message = 'Your order has been cancelled !!'
        messages.success(request, error_message)
        return redirect('profile')
