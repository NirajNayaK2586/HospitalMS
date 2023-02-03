from django.contrib import admin

from .models import ChildCare, HealthPackages, HealthPackageMain

admin.site.register(ChildCare)
admin.site.register(HealthPackageMain)
admin.site.register(HealthPackages)