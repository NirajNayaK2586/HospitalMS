from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

class ChildCare(models.Model):
    childcaretitle = models.CharField(max_length=50)
    description = RichTextField()
    showcase_image = models.FileField(upload_to='childcare_image', blank=True)
    schedule_image = models.FileField(upload_to='childcare_image_schedule', blank=True, null=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.childcaretitle


class HealthPackageMain(models.Model):
    """ This is to create a major package e.g. Women Health Checkup Package """
    package_title_main = models.CharField(max_length=50)
    image = models.FileField(upload_to='package_image_main', blank=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package_title_main

class HealthPackages(models.Model):
    """ This is to create packages under a major package E.g. Diabetes Package, Women's Health Screening Package """
    MainPackage = models.ForeignKey(HealthPackageMain, on_delete=models.CASCADE)
    package_title = models.CharField(max_length=50)
    description = RichTextField()
    image = models.FileField(upload_to='package_image', blank=True)
    added_date = models.DateTimeField(auto_now=True)
    package_price = models.IntegerField(default=5000)
    total_tests = models.IntegerField(default=5)
    # add widget for text edit
    def __str__(self):
       return self.package_title