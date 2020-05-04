"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pages.views import PagesView, home_view
from products.views import cart_view, cart_buy_view, update_product_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('', home_view, name='home'),
    path('contact/', PagesView.as_view(template_name='contact.html'), name='contact'),
    path('social/', PagesView.as_view(template_name='social.html'), name='social'),
    path('about/', PagesView.as_view(template_name='about.html'), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', PagesView.as_view(template_name='user/profile.html'), name='profile'),
    path('cart/', cart_view, name='cart'),
    path('cart/buy', cart_buy_view, name='cart_buy'),
    path('cart/update', update_product_cart, name='cart_update')


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
