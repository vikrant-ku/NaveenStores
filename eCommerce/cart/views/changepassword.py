from django.views import  View
from django.shortcuts import render , redirect
from cart.models.customer import Customer
from django.contrib.auth.hashers import  check_password , make_password
from django.contrib import messages


class Change_password(View):

    def get(self , request):
       return redirect('profile')

    def post(self, request):
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        customer = Customer.get_customer_by_id(request.session.get('customer_id'))

        if  check_password(password, customer.password):

            customer.password = new_password
            customer.password = make_password(customer.password)
            customer.register()

            error_message = "Your Password Successfully Changed"
            messages.success(request, error_message)
            return redirect('profile')
        else:
            error_message = "Password do not match please try again"
            messages.error(request, error_message)
            return redirect('profile')