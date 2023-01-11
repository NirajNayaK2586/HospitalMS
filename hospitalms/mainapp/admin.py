from django.contrib import admin

from .models import CustomUser, Role, Doctor, Receptionist, Patient, Appointments, Report, ReviewComment, Bills

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(Role)
admin.site.register(Appointments)
admin.site.register(ReviewComment)
admin.site.register(Report)
admin.site.register(Bills)
