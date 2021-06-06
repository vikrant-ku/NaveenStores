from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from django.http import HttpResponseRedirect
from cart.models.customer import Customer
from django.contrib import messages
from django.core.mail import EmailMessage
from .pages import card_len
import string
import random


class Signup(View):
    def get(self, request):
        len_cart = card_len

        cart_prod = {
            'len': len_cart,
        }
        messages.success(request,  request.session.get('customer'))
        return render(request, 'signup.html', cart_prod)

    def post(self, request):
        postData = request.POST
        customer_name = postData.get('register-name')
        phone = postData.get('register-phone')
        email = postData.get('register-email')
        password = postData.get('register-password')
        password1 = postData.get('register-repassword')
        error_message = None

        customer = {'customer_name':customer_name,
                            'phone':phone,
                            'email':email,
                            'password':password,
                            'password1': password1}
        error_message = self.validateCustomer(customer)

        if not error_message:
            otp = Signup.random_password(self, 6)
            email = EmailMessage('OTP', f'Your One Time Password is :"{otp}" . ', to=[email])
            email.send()
            customer['otp'] = otp
            return render(request, 'validate_customer.html',  {'customer': customer})
        else:
            messages.error(request, error_message)
            return render(request, 'signup.html',)

    def validateCustomer(self, customer):
        error_message = None
        if not customer['customer_name']:
            error_message = "Name  Required !!"
        elif len(customer['customer_name']) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer['phone']:
            error_message = 'Phone Number required'
        elif len(customer['phone']) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif customer['password'] != customer['password1']:
            error_message = 'Password do not match'
        elif len(customer['password']) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer['email']) < 5:
            error_message = 'Email must be 5 char long'
        elif Customer.isExists(customer['email']):
            error_message = 'Email Address Already Registered..'
        return error_message

    def random_password(self, n):

        LETTERS = string.ascii_letters
        NUMBERS = string.digits
        PUNCTUATION = '@#$&'

        printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
        printable = list(printable)
        random.shuffle(printable)
        random_password = random.choices(printable, k=n)
        random_password = ''.join(random_password)

        return random_password

def validate_email(request):
    if request.method == 'POST':
        postData = request.POST
        customer_name = postData.get('customer_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        otp = postData.get('otp')
        user_otp = postData.get('user_otp')
        if otp == user_otp:
            customer = Customer(customer_name=customer_name, phone=phone, email=email,password=password)
            customer.password = make_password(customer.password)
            customer.register()
            request.session['customer_id'] = customer.id
            request.session['customer_name'] = customer.customer_name
            return redirect('home')
        else:
            error_message = "Invalid OTP"
            messages.error(request, error_message)
            return redirect('validate_email')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





