from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from cart.models.customer import Customer, Cart
from django.views import  View
from django.contrib import messages
from .pages import card_len


class Login(View):
    return_url = None
    def get(self , request):
        len_cart = card_len(request)
        url = request.GET.get('return_url')
        if url:
            self.return_url = url
        try:
            user = request.session.get('customer_id')
        except:
            user = None
        if user:
            return redirect("home")
        else:

            cart_prod = {
                'len': len_cart,
            }
            Login.return_url = request.GET.get('return_url')
            return render(request , 'login.html', cart_prod)

    def post(self, request):
        email = request.POST.get('login-email')
        password = request.POST.get('login-password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)

            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_name'] = customer.customer_name
                error_message = 'Login Successful !!'
                messages.success(request, error_message)
                cart = load_cart_DB_to_session(int(customer.id))

                request.session['cart'] = cart
                if Login.return_url:

                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        messages.error(request, error_message)
        return redirect('login')


def logout(request):
    request.session.clear()
    return redirect('home')



# save session cart to database
def save_cart(request):
    user_id = int(request.session.get('customer_id'))
    User = Customer.objects.get(id =user_id)
    user_cart = None
    user = 0
    try:
        user_cart = request.session.get('cart')
    except:
        pass
    if user_cart != None:
        try:
            user = Cart.objects.get(user=user_id)
        except:
            pass
        cart = ""
        for i in user_cart:
            cart += str(i) + ","
            cart += str(user_cart[i][0]) + ","
            cart += str(user_cart[i][1]) + ","

        if user == 0:
            user = Cart(user=User, cart=cart)
            user.register()
        else:
            user.cart = cart
            user.register()



def load_cart_DB_to_session(customer_id):
    try:
        user_cart = Cart.objects.get(user=customer_id)
    except:
        user_cart= None
    if user_cart:

        cart = {}
        user_cart = user_cart.cart.split(",")
        for i in range(0, len(user_cart) - 1, 3):
            prod_info = []
            prod_info.append(user_cart[i + 1])
            prod_info.append(user_cart[i + 2])
            cart[user_cart[i]] = prod_info
        return cart
    else:
        return user_cart





