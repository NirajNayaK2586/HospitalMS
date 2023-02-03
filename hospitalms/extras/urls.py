from django.urls import path

from .views import health_packages, health_packagess
from . import views

app_name='extras'
urlpatterns = [
    path('health-packages', views.health_packages, name='health_packages'),

    # Health packages Main vhitrako heal packages
    path('health-packagess/<int:id>', views.health_packagess, name='health_packagess'),

    path('sp-health-packagess/<int:id>', views.sp_health_packagess, name='sp_health_packagess'),
]