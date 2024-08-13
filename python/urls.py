"""python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import HungrezyApp.views as hungrezy_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', hungrezy_views.home),
    
    path('', hungrezy_views.home),

    path('restaurants/', hungrezy_views.restaurants),

    path('restaurants/menu/', hungrezy_views.menu),

    path('homemade-food-options/', hungrezy_views.homemadefoodoptions),

    path('category/', hungrezy_views.category),

    path('about-us/', hungrezy_views.aboutus),

    path('contact/', hungrezy_views.contact),

    path('login/', hungrezy_views.login),

    # path('admin/', hungrezy_views.admin),

    path('admin/update-restaurant/', hungrezy_views.updaterestaurant),

    path('admin/update-rider/', hungrezy_views.updaterider),

    path('admin/update-customer/', hungrezy_views.updatecustomer),

    path('admin/update-rider-status/', hungrezy_views.updateriderstatus),

    path('admin/update-admin-profile/', hungrezy_views.updateadminprifile),

    path('rider/', hungrezy_views.rider),

    path('rider/update-rider-profile/', hungrezy_views.updateriderprofile),

    path('rider/rider-salary/', hungrezy_views.ridersalary),

    path('rider/rider-history/', hungrezy_views.riderhistory),

    path('restaurant-owner/', hungrezy_views.restaurantowner),

    path('restaurant-owner/update-owner-profile/', hungrezy_views.updateownerprofile),

    path('restaurant-owner/update-restaurant/', hungrezy_views.ownerupdaterestaurant),

    path('restaurant-owner/update-price/', hungrezy_views.updateprice),

    path('restaurant-owner/update-menu/', hungrezy_views.updatemenu),

    path('customer/', hungrezy_views.customer),

    path('customer/update-customer-profile/', hungrezy_views.updatecustomerprofile),

    path('customer/order/', hungrezy_views.order),

    path('customer/rating/', hungrezy_views.rating),

    path('customer/review/', hungrezy_views.review),

    path('homemade-food-supplier/', hungrezy_views.homemadefoodsuppiler),

    path('homemade-food-supplier/update-supplier-profile/', hungrezy_views.updatesuppilerprofile),

    path('homemade-food-supplier/update-homemade-food-price/', hungrezy_views.updatehomemadefoodprice),

    path('homemade-food-supplier/update-homemade-food-options/', hungrezy_views.updatehomemadefoodoptions),

    path('signup/', hungrezy_views.signup),

    path('signup-as/', hungrezy_views.signupas),

    path('customer-account-signup/', hungrezy_views.customeraccountsignup),

    path('business-account-signup/', hungrezy_views.businessaccountsignup),

    path('rider-account-signup/', hungrezy_views.rideraccountsignup),
    
    path('customer-info-update/', hungrezy_views.customerupdateinfo),
    
    path('business-info-update/', hungrezy_views.businessaccinfoupdate),
    
    path('rider-info-update/', hungrezy_views.rideraccountinfoupdate),
    
    # path('customer-login/', hungrezy_views.customerlogin),
    
    path('order-process/', hungrezy_views.menucart),
    
    
]
