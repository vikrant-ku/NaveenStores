from django.views import  View
from django.shortcuts import render
from cart.models.product import Product
from .pages import card_len

class Product_detail(View):

    def get(self , request , id):
        len_cart = card_len(request)

        prod = Product.objects.get(id=id)
        prodname = prod.name
        prodname = prodname.split("_")
        related_prod = Product.objects.filter(name__icontains=prodname[0])

        ids =[]
        try:
            if request.session.get("cart"):
                ids = list(request.session.get('cart').keys())
        except:
            pass
        flag = ""
        if str(id) in ids:
            flag = 1
        my_product = {
            'product': prod,
            'flag' : flag,
            'len': len_cart,
            'related_prod':related_prod

                }
        return render(request , 'product_view.html', my_product)
