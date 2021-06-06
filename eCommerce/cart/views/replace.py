from django.views import  View
from django.shortcuts import render , redirect
from cart.models.customer import Customer
from cart.models.orders import Orders
from django.core.files.storage import FileSystemStorage
from cart.models.replace import Replace
from . pages import card_len
from django.contrib import messages


class Replace_prod(View):
    def get(self, request, id):
        len_cart = card_len(request)

        try:
            user = request.session.get('customer_id')
        except:
            user = False
        if user:

            order = Orders.get_order_by_id(id)
            if order:
                if order.status == 'Delivered':
                    cart_prod = {

                        'len': len_cart,
                        'order': order
                    }
                    return render(request, 'replace.html',cart_prod)
                else:
                    return redirect('profile')
            else:
                return redirect('profile')
        else:
            return redirect('home')

    def post(self, request):
        image = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(image.name, image)
        customer = request.session.get('customer_id')
        order_id = request.POST.get('order_id')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        reason = request.POST.get('reason')

        replace_detail = Replace(customer=Customer(id=customer), order_id= order_id, image=image.name, phone=phone, email=email, reason=reason)
        replace_detail.save()
        order = Orders.get_order_by_id(int(order_id))
        order.status = "Replace"
        order.register()
        error_message = 'your replace request has been completed !!'
        messages.error(request, error_message)
        return redirect('profile')
