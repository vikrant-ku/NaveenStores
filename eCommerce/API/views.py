from rest_framework import viewsets
from django.contrib.auth.hashers import check_password, make_password
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import Category_serilizer, Customer_serilizer, Contact_serilizer, Product_serilizer , Oreder_serilizer, UserLoginSerializer
from .serializers import Cart_serilizer, Billing_serilizer, Cancel_order_serilizer, Replace_serilizer, Subscriber_serilizer, EmailVerificationSerializer
from .serializers import UserChangePasswordSerializer, UserResetPasswordSerializer, FacebookLive_serilizer, Payment_serilizer
from cart.models.category import Category
from cart.models.payment import Payment
from cart.models.customer import Customer, Cart
from cart.models.contact_us import Contact
from cart.models.product import Product,  FbLive
from cart.models.orders import Orders
from cart.models.billing import Billing
from cart.models.cancle_order import Cancel_order
from cart.models.replace import Replace
from cart.models.subscribers import Subscriber
from cart.views.signup import Signup
from django.core.mail import EmailMessage
from django.http import JsonResponse

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_serilizer
    filterset_fields = ['Name']
    http_method_names = ['get']


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_serilizer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Contact_serilizer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serilizer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'subcat_type', 'type']
    http_method_names = ['get']

class FacebookLiveViewSet(viewsets.ModelViewSet):
    queryset =FbLive.objects.all()
    serializer_class = FacebookLive_serilizer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']
    http_method_names = ['get']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Oreder_serilizer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cart_serilizer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = Billing_serilizer


class Cancel_orderViewSet(viewsets.ModelViewSet):
    queryset = Cancel_order.objects.all()
    serializer_class = Cancel_order_serilizer

class ReplaceViewSet(viewsets.ModelViewSet):
    queryset = Replace.objects.all()
    serializer_class = Replace_serilizer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = Subscriber_serilizer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Payment_serilizer

class VerifyEmail(viewsets.ViewSet):
    serializer_class = EmailVerificationSerializer
    http_method_names = ['get','post']
    data = {}
    def get_queryset(self):
        return JsonResponse(self.data)

    def create(self, request):
        email = request.data['email']
        try:
            user = Customer.objects.get(email=email)
        except:
            user = None
        if user != None:
            self.data['error']='email is already exist.'
            return JsonResponse(self.data)
        else:
            otp = Signup.random_password(self, 6)
            email = EmailMessage('OTP', f'Your One Time Password is :"{otp}" . ', to=[email])
            email.send()
            self.data['error']=otp
            return JsonResponse(self.data)


class UserLogin(viewsets.ViewSet):
    serializer_class = UserLoginSerializer
    http_method_names = ['get', 'post']
    data = {}
    def get_queryset(self):
        return JsonResponse(self.data)

    def create(self, request):

        email = request.data['email']
        password = request.data['password']
        try:
            user = Customer.objects.get(email=email)
        except:
            user = None
        if user != None:
            flag = check_password(password, user.password)
            if flag:
                self.data["id"] = user.id
                self.data["name"] = user.customer_name
                self.data["phone"] = user.phone
                self.data["email"] = user.email
                return JsonResponse(self.data)
            return JsonResponse({'error': 'Password Do not Match'})
        else:
            return JsonResponse({'error': 'User is not Exist '})


class UserChangePassword(viewsets.ViewSet):
    serializer_class = UserChangePasswordSerializer
    http_method_names = ['get', 'post']
    data = {}
    def get_queryset(self):
        return JsonResponse(self.data)

    def create(self, request):
        email = request.data['email']
        old = request.data['oldpassword']
        new = request.data['newpassword']
        try:
            user = Customer.objects.get(email=email)
        except:
            user = None
        if user != None:
            flag = check_password(old, user.password)
            if flag:
                user.password = new
                user.password = make_password(user.password)
                user.save()
                self.data['user']="Password Successfully Changed"
                return JsonResponse(self.data)
            self.data['user']=" t Match"
            return JsonResponse(self.data)
        else:
            self.data['user']="Email is not valid"
            return JsonResponse(self.data)


class UserResetPassword(viewsets.ViewSet):
    serializer_class = UserResetPasswordSerializer
    data = {}
    def get_queryset(self):
        return JsonResponse(self.data)
    def create(self, request):
        email = request.data['email']
        try:
            user = Customer.objects.get(email=email)
        except:
            user = None
        if user != None:
            newpass = Signup.random_password(self, 10)
            user.password = newpass
            user.password = make_password(user.password)
            user.save()
            email = EmailMessage('OTP', f'Your New Password is :"{newpass}" . ', to=[email])
            email.send()
            self.data["user"]="success"
            return JsonResponse(self.data)
        else:
            self.data["user"] = "Email is not valid"
            return JsonResponse(self.data)









