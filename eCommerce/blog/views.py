from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views import View


class Blog_post(View):
    def get(self, request):

        len_cart = card_len(request)
        try:
            posts = Blog.objects.filter(status = "Posted").order_by("-date")
        except:
            posts= None
        paginator = Paginator(posts, 3)
        page = request.GET.get('page')

        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)

        if page is None:
            start_index = 0
            end_index = 7
        else:
            (start_index, end_index) = proper_pagination(post, index=1)

        page_range = list(paginator.page_range)[start_index:end_index]


        param= {
            'blog':post,
            'page_range': page_range,
            'len': len_cart,
        }
        return render(request, 'blog.html', param)


class Post_view(View):
    def get(self, request,slug ):
        len_cart = card_len(request)
        post = Blog.objects.get(slug=slug)
        return render(request, 'blog_view.html', {'post': post,  'len': len_cart})

def card_len(request):
    cart = 0
    try:
        cart = request.session.get("cart")
        return len(cart)

    except:
         return cart

def proper_pagination(post, index):
    start_index = 0
    end_index = 7
    if post.number > index:
        start_index = post.number - index
        end_index = start_index + end_index
    return (start_index,end_index)


def error_404(request, exception):
   context = {}
   return render(request,'404.html', context)

def error_500(request):
   context = {}
   return render(request,'500.html', context)





