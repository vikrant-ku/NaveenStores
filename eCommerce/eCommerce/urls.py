from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from blog import views


admin.site.site_header = 'Naveen Store admin'
admin.site.site_title = 'Naveen Store admin'
admin.site.site_url = 'http://naveenstore.com/'
admin.site.index_title = 'Naveen Store administration'
admin.empty_value_display = '**Empty**'

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cart.urls')),
    path('blog/', include('blog.urls')),
    path('rohar/tech/naveen/api/', include('API.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


