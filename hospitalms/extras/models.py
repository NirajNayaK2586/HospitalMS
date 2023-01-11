from django.db import models

class ChildCare(models.Model):
    childcaretitle = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='childcare_image', blank=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.childcaretitle

class HealthPackages(models.Model):
    package_title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='package_image', blank=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.package_title