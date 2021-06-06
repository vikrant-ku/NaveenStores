from django.views import  View
from django.shortcuts import render , redirect
from cart.models.product import Product
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .pages import card_len

class Search(View):

    def get(self , request, filter=None):

        len_cart = card_len(request)

        my_product = {}

        query = request.GET.get('q', None)
        if query != None:
            if filter !=None and filter=="Low to High":
                prod = Product.objects.filter(Q(name__icontains=query)
                                              | Q(subcat_type__icontains=query)
                                              | Q(category__Name__icontains=query)
                                              | Q(subcategory__icontains=query)
                                              | Q(description__icontains=query)
                                              ).order_by('discount_price')

            elif filter !=None and filter=="High to Low":
                prod = Product.objects.filter(Q(name__icontains=query)
                                              | Q(subcat_type__icontains=query)
                                              | Q(category__Name__icontains=query)
                                              | Q(subcategory__icontains=query)
                                              | Q(description__icontains=query)
                                              ).order_by('-discount_price')
            else:
                prod = Product.objects.filter(Q(name__icontains=query)
                                              | Q(subcat_type__icontains=query)
                                              | Q(category__Name__icontains=query)
                                              | Q(subcategory__icontains=query)
                                              | Q(description__icontains=query)
                                                )
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


            my_product = {"searchprods": prods,
                          "q": query,
                          'page_range': page_range,
                          'len': len_cart,
                          'filter':filter
                          }

        return render(request, 'search.html', my_product)


def proper_pagination(prods, index):
    start_index = 0
    end_index = 7
    if prods.number > index:
        start_index = prods.number - index
        end_index = start_index + end_index
    return (start_index,end_index)



