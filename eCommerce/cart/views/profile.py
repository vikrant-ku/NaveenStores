from django.views import  View
from django.shortcuts import render, redirect
from cart.models.customer import Customer
from cart.models.orders import Orders
from cart.models.billing import Billing
from .pages import card_len

class Profile(View):

    def get(self , request):
        len_cart = card_len(request)
        orders= None
        try:
            orders = Orders.objects.filter(customer_id = request.session.get('customer_id')).order_by('-order_date')
        except:
            pass
        customer = Customer.objects.get(id = request.session.get('customer_id'))


        billing = Billing.get_bill_address_by_id(request.session.get("customer_id"))

        cart_prod = {
                'orders': orders,
                'customer': customer,
                'billing': billing,
                'len': len_cart,
            }
        return render(request , 'profile.html',cart_prod)

class User_billing(View):
    def get(self):
        return redirect('profile')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal-code')
        phone = request.POST.get('phone')
        user_address = Billing.get_bill_address_by_id(request.session.get("customer_id"))

        if not user_address:
            billing_address = Billing(user=Customer(request.session.get('customer_id')), name=name, email=email,
                                      country=country, state=state,
                                      address1=address1, address2=address2, city=city, zip_code=postal_code,
                                      phone=phone)
            billing_address.save()
        else:
            user_address.name = name
            user_address.email = email
            user_address.country = country
            user_address.state = state
            user_address.address1 = address1
            user_address.address2 = address2
            user_address.city = city
            user_address.zip_code = postal_code
            user_address.phone = phone
            user_address.save()
        
        return redirect('profile')


class User_info(View):
    def post(self, request):
        postData = request.POST
        customer = Customer.get_customer_by_id(request.session.get('customer_id'))
        customer_name = postData.get('name')
        phone = postData.get('phone')
        customer.customer_name = customer_name
        customer.phone = phone
        customer.save()
        request.session['customer_name'] = customer.customer_name
        return redirect('profile')