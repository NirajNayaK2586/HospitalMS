from django.contrib import admin

from .models import ChildCare, HealthPackages

admin.site.register(ChildCare)
admin.site.register(HealthPackages)