from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib import messages
from cart.models.contact_us import Contact
from cart.models.subscribers import Subscriber

class About_us(View):
    def get(self, request):

        length = card_len(request)
        cart_prod = {
            'len': length
        }
        return render(request, 'about_us.html', cart_prod)

class FAQ(View):
    def get(self, request):
        length = card_len(request)
        cart_prod = {
            'len': length
        }
        return render(request, 'faqs.html', cart_prod )

class Terms(View):
    def get(self, request):
        length = card_len(request)
        cart_prod = {
            'len': length
        }
        return render(request, 'terms_condition.html', cart_prod )

class Contact_us(View):
    def get(self, request):
        length = card_len(request)
        cart_prod = {
            'len': length
        }
        return render(request, 'contact_us.html', cart_prod )

    def post(self, request):
        Message = ''
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if  not str(phone).isdigit():
            Message = "Please Enter valid Mobile number."
            messages.error(request, Message)
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.register()
            Message = "Your Message Has been send. We will Get back to you soon..."
            messages.success(request, Message)
        return redirect('contact')

class Subscribers(View):
    def post(self, request):
        returnUrl = request.META['PATH_INFO']
        email = request.POST.get('subscribe-email')
        try:
            subscr = Subscriber.objects.get(email=email)
        except:
            subscr= None
        if subscr== None:
            subscriber = Subscriber(email=email)
            subscriber.save()
            return HttpResponseRedirect(returnUrl)
        else:
            Message = "Your are already Subscribed."
            messages.success(request, Message)
            return HttpResponseRedirect(returnUrl)

def card_len(request):
    cart = 0
    try:
        cart = request.session.get("cart")
        return len(cart)

    except:
         return cart





