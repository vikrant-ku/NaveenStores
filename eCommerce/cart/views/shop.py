from django.shortcuts import render, get_object_or_404
from cart.models.product import Product , FbLive
from cart.models.category import Category
from rest_framework.views import APIView
from .pages import card_len
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage



class Shop(APIView):

    def get(self , request, category, subcat= None, filter = None):

        len_cart = card_len(request)
        if subcat == "Low-to-High" or filter == "Low-to-High":
            cat = Category.objects.get(Name=category)
            if subcat and subcat != "Low-to-High":
                pro = []
                prod_by_cat = Product.objects.filter(category=cat.id).order_by('discount_price')
                for i in prod_by_cat:
                    if i.subcategory.lower() == subcat.lower() or i.subcat_type.lower() == subcat.lower():
                        pro.append(i)
                prod = pro
            else:
                prod = Product.objects.filter(category=cat.id).order_by('discount_price')
        elif subcat == "High to Low" or filter == "High to Low":
            cat = Category.objects.get(Name=category)
            if subcat and subcat != "High to Low":
                pro = []
                prod_by_cat = Product.objects.filter(category=cat.id).order_by('-discount_price')
                for i in prod_by_cat:
                    if i.subcategory.lower() == subcat.lower() or i.subcat_type.lower() == subcat.lower():
                        pro.append(i)
                prod = pro
            else:
                prod = Product.objects.filter(category=cat.id).order_by('-discount_price')
        else:
            cat = get_object_or_404(Category, Name=category)

            if subcat:
                pro = []
                prod_by_cat = Product.objects.filter(category = cat.id)
                for i in prod_by_cat:
                    if i.subcategory.lower() == subcat.lower() or i.subcat_type.lower() == subcat.lower():
                        pro.append(i)
                prod = pro
            else:
                prod = Product.objects.filter(category= cat.id).order_by('id')


        #paginator
        paginator = Paginator(prod, 3)
        page = request.GET.get('page')

        try:
            prods = paginator.page(page)
        except PageNotAnInteger:
            prods = paginator.page(1)
        except EmptyPage:
            prods = paginator.page(paginator.num_pages)

        if page is None:
            start_index = 0
            end_index= 7
        else:
            (start_index, end_index)=proper_pagination(prods, index=1)

        page_range = list(paginator.page_range)[start_index:end_index]

        my_product = {
            'allprods': prods,
            'len': len_cart,
            'page_range': page_range,
            'category':category,
            'subcategory':subcat,
            'filter': filter,
                    }

        return render (request, 'shop.html', my_product)


class Fbshop(APIView):
    def get(self, request, date=None):

        dates = FbLive.objects.order_by('-date').values_list('date', flat=True).distinct()
        fbprod= ""

        if date:
            fbprod = FbLive.objects.filter(date= date)
            pass
        else:
            fbprod = FbLive.objects.all().order_by('-date')

        prod = []

        for _ in fbprod:
            prod.append(get_object_or_404(Product, sr_no=_.prodsr_no))

        paginator = Paginator(prod, 3)
        page = request.GET.get('page')

        try:
            prods = paginator.page(page)
        except PageNotAnInteger:
            prods = paginator.page(1)
        except EmptyPage:
            prods = paginator.page(paginator.num_pages)

        if page is None:
            start_index = 0
            end_index = 7
        else:
            (start_index, end_index) = proper_pagination(prods, index=1)

        page_range = list(paginator.page_range)[start_index:end_index]

        len_cart = card_len(request)
        my_product = {
            'allprods': prods,
            'len': len_cart,
            'date': dates,
            'page_range': page_range,
            'filterdate': date
        }
        return render(request, 'fbshop.html', my_product)

def proper_pagination(prods, index):
    start_index = 0
    end_index = 7
    if prods.number > index:
        start_index = prods.number - index
        end_index = start_index + end_index
    return (start_index,end_index)