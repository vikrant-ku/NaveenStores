from django.views import  View
from django.http import HttpResponse
from django.shortcuts import render , redirect, reverse
from cart.models.orders import Orders
from cart.models.product import Product
from cart.models.customer import Customer
from cart.models.payment import Payment
from django.contrib import messages
from cart.models.customer import  Cart
from cart.models.billing import  Billing
from .pages import card_len
import datetime
##########
import json
import razorpay
from django.conf import settings
keyid = settings.RAZORPAY_KEYID
keysecret = settings.RAZORPAY_KEYSECRET
razorpay_client = razorpay.Client(auth=(keyid, keysecret))




class Billing_shipping(View):

    def get(self , request):
        len_cart = card_len(request)
        cart = None
        cart_prod = {}
        try:
            cart = request.session.get('cart')
        except:
            pass
        if cart:
            product = []
            for id, value in cart.items():
                product.append(id)
                product.append(value)
            ids = list(request.session.get('cart').keys())
            if ids:

                products = Product.get_products_by_id(ids)

                user_address = Billing.get_bill_address_by_id(request.session.get("customer_id"))


                cart_prod = {
                "pro": products,
                'len': len_cart,
                'user_address': user_address,
                            }
                return render(request, 'billing-shipping.html', cart_prod)

        return redirect('home')

    def post(self , request):
        len_cart = card_len(request)
        user_cart = request.session.get('cart')
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        phone = request.POST.get('phone')
        totalprice = int(request.POST.get('total_price'))

        user_address = Billing.get_bill_address_by_id(request.session.get("customer_id"))
        # save user billing address
        if not user_address:
            billing_address = Billing(user = Customer(request.session.get('customer_id')),name=name, email=email, country=country, state=state,
                               address1=address1, address2=address2, city=city, zip_code=postal_code, phone=phone)
            billing_address.save()

        # create payment
        payment = razorpay_client.order.create({'amount': totalprice * 100, "currency": "INR", "payment_capture": "1"})

        pymnt= Payment(user=Customer(id=request.session.get('customer_id')),razorpay_order_id=payment.get('id'), amount=totalprice)
        pymnt.save()

        products = Product.get_products_by_id(list(user_cart.keys()))
        for product in products:
            order = Orders(
                    customer =Customer(id=request.session.get('customer_id')),
                    payment = pymnt,
                    product= product,color =user_cart.get(str(product.id))[1], quantity=user_cart.get(str(product.id))[0],
                    price=get_price(product,user_cart.get(str(product.id))[0]),
                    name=name, email=email, country=country, state=state,
                    address=address1+" "+address2, city=city, zip_code=postal_code,
                    phone=phone)
            order.save()

        callback_url = request.build_absolute_uri()+"payment_status/"


        data = {'amount':totalprice,"orderid": payment.get('id'), "callback_url": callback_url, "keyid": keyid}
        response = json.dumps(data, default=str)
        return HttpResponse(response)

                ## update product stock
                # product.stock -= int(user_cart.get(str(product.id))[0])
                # product.save()

        # return redirect('billing_shipping')

def get_price(product, quantity):
    if product.discount_price > 0:
        return int(product.discount_price)*int(quantity)
    else:
        return int(product.price)*int(quantity)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handlerequest(request):
    len_cart = card_len(request)
    if request.method == "POST":
        data = request.POST
        payment_id = data.get('razorpay_payment_id')
        order_id = data.get('razorpay_order_id')
        signature = data.get('razorpay_signature')
        params_dict = {
        'razorpay_order_id': order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
        }
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        if result is None:
            payment = Payment.objects.get(razorpay_order_id=order_id)
            payment.razorpay_payment_id=payment_id
            payment.date = datetime.datetime.now()
            payment.save()
            # empty cart
            request.session.pop('cart')
            try:
                user = Cart.objects.get(user=Customer(request.session.get('customer_id')))
                user.cart = ''
                user.save()
            except:
                pass

            ## update product stock
            update_product_stock(order_id)


            return render(request, 'payment_done.html',{ 'len': len_cart})
        else:
            return render(request, 'payment_cancelled.html',{ 'len': len_cart})




def update_product_stock(razorpay_order_id):
    payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
    orders = Orders.objects.filter(payment=payment)
    for order in orders:
        prod = Product.objects.get(pk = order.product.id)
        prod.stock -= int(order.quantity)
        prod.save()

