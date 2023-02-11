from django.urls import path

from .views import health_packages, health_packagess
from . import views

app_name='extras'
urlpatterns = [
    path('health-packages', views.health_packages, name='health_packages'),

    # Health packages Main vhitrako heal packages
    path('health-packagess/<int:id>', views.health_packagess, name='health_packagess'),

    path('sp-health-packagess/<int:id>', views.sp_health_packagess, name='sp_health_packagess'),

    # Buy package ko url
    path('buy_package/<int:id>', views.buy_package, name='buy_package'),

    path('verify_bill/<int:id>', views.verify_bill, name='verify_bill'),
    path('khalti_verify_bill/<int:id>', views.khalti_verify_bill, name='khalti_verify_bill'),


    path('childcare', views.childcare, name='childcare'),
    path('childcaredetails/<int:id>', views.childcaredetails, name='childcaredetails'),

    path('about', views.about, name='about'),


]