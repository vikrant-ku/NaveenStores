from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.views import  View
from cart.models.product import Product
from .login import save_cart , load_cart_DB_to_session
from .pages import card_len


class Cart(View):
    def get(self , request):
        len_cart = card_len(request)
        cart = load_cart_DB_to_session(int(request.session['customer_id']))
        request.session['cart'] = cart
        try:
            cart = request.session.get('cart')
        except:
            cart = None
        if cart != None:
            ids = list(cart.keys())
            products = Product.get_products_by_id(ids)
            updatecart = {}
            for key, value in cart.items():
                prod = get_object_or_404(Product, id=int(key))
                if int(value[0]) > int(prod.stock):
                    value[0] = str(prod.stock)
                    updatecart[key] = value
                else:
                    updatecart[key] = value

            request.session['cart'] = updatecart
            save_cart(request)

        else:
            products = None
        cart_prod = {
            "pro": products,
            'len': len_cart
        }
        return render(request, 'cart.html', cart_prod)

    def post(self, request):
        p_quantity = request.POST.get("quantity")
        p_id = request.POST.get("product_id")
        p_color = request.POST.get("product_color")

        cart = request.session.get("cart")

        if cart:
            cart[p_id] = [p_quantity, p_color]

        else:
            cart = {}
            cart[p_id] = [p_quantity, p_color]
        request.session['cart'] = cart
        save_cart(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_item(request, id):
    cart = request.session.pop('cart')
    cart.pop(str(id))
    request.session['cart'] = cart
    save_cart(request)
    return redirect('cart')

def update_item(request):
    if request.method == 'POST':
        p_id = str(request.POST.get('p_id'))
        p_quantity = str(request.POST.get('quantity'))
        cart = request.session.pop('cart')
        cart[p_id][0] = p_quantity
        request.session['cart'] = cart
        save_cart(request)
        return redirect('cart')

















