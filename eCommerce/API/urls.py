from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, CustomerViewSet, ContactViewSet, ProductViewSet, OrderViewSet , UserChangePassword, UserResetPassword, PaymentViewSet
from .views import CartViewSet, BillingViewSet, Cancel_orderViewSet, ReplaceViewSet, SubscriberViewSet, VerifyEmail, UserLogin, FacebookLiveViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'contact_us', ContactViewSet)
router.register(r'product', ProductViewSet)
router.register(r'fblive',FacebookLiveViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'cancel_order', Cancel_orderViewSet)
router.register(r'replace', ReplaceViewSet)
router.register(r'subscriber', SubscriberViewSet)
router.register(r'user-login', UserLogin, basename='user_login')
router.register(r'email-verify', VerifyEmail, basename='email-verify')
router.register(r'user-change-password', UserChangePassword, basename='user-change-password')
router.register(r'user-reset-password', UserResetPassword, basename='user-reset-password')

urlpatterns = [
      path('', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

   ]

