from django.urls import path
from .views.home import Index
from .views.cart import Cart, delete_item, update_item
from .views.shop import Shop , Fbshop
from .views.order_cancellation import Order_cancel
from .views.replace import Replace_prod
from .views.search import Search
from .views.signup import Signup, validate_email
from .views.login import Login, logout
from .views.profile import Profile, User_billing, User_info
from .views.pages import About_us, FAQ, Contact_us, Terms, Subscribers
from .views.changepassword import Change_password
from .views.forgetpassword import Forget_password
from .views.billing_shipping import Billing_shipping, handlerequest
from .views.product_detail import Product_detail
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('cart/',  auth_middleware(Cart.as_view()), name='cart'),
    path('facebookLive/', Fbshop.as_view()),
    path('facebookLive/<str:date>/', Fbshop.as_view()),
    path('facebookLive/<str:date>/<str:filter>/', Fbshop.as_view()),
    path('shop/<str:category>/', Shop.as_view(), name='shop'),
    path('shop/<str:category>/<str:subcat>/', Shop.as_view(), name='shop'),
    path('shop/<str:category>/<str:subcat>/<str:filter>/', Shop.as_view(), name='shop'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signup/validate/', validate_email, name='validate_email'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', auth_middleware(Profile.as_view()), name='profile'),
    path('profile/update_user_info/', auth_middleware(User_info.as_view()), name='update_user'),
    path('profile/billing_shipping/', auth_middleware(User_billing.as_view()), name='profile-billing'),
    path('profile/order/order_cancellation/<int:id>', Order_cancel.as_view()),
    path('profile/order/order_cancellation', Order_cancel.as_view()),
    path('profile/order/order_replace/<int:id>', Replace_prod.as_view()),
    path('profile/order/order_replace', Replace_prod.as_view()),
    path('profile/change_password/', auth_middleware(Change_password.as_view()), name='change_password'),
    path('login/forget_password/', Forget_password.as_view(), name='forget_password'),
    path('cart/billing_shipping/', auth_middleware(Billing_shipping.as_view()), name='billing_shipping'),
    path('cart/billing_shipping/payment_status/', handlerequest, name='billing_shipping_payment'),
    path('product_detail/<int:id>', Product_detail.as_view(), name='product_detail'),
    path('cart/<int:id>', auth_middleware(delete_item), name='delete_item'),
    path('cart/update_item/', update_item, name='update_item'),
    path('about_us/', About_us.as_view(), name='about'),
    path('subscriber/', Subscribers.as_view(), name='subscribers'),
    path('contact_us/', Contact_us.as_view(), name='contact'),
    path('faqs/', FAQ.as_view(), name='faqs'),
    path('terms/', Terms.as_view(), name='terms'),
    path('search/', Search.as_view(), name='search'),
    path('search/<str:filter>/', Search.as_view(), name='search'),
    path('logout/', logout, name='logout'),
   ]

