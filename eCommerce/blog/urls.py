from django.urls import path, include
from .views import Blog_post,Post_view

urlpatterns = [

    path('', Blog_post.as_view(), name='bloghome'),
    path('post/<str:slug>', Post_view.as_view(), name='post'),
   ]

