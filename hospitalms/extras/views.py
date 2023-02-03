from django.shortcuts import render
from .models import HealthPackageMain, HealthPackages, ChildCare


def health_packages(request):
    template_name = 'extras/health_packages.html'
    hpmain = HealthPackageMain.objects.all()

    return render(request, template_name, {'hpmains': hpmain})


def health_packagess(request, id):
    template_name = 'extras/health_packagess_list.html'

    hp = HealthPackageMain.objects.get(id=id)
    # Save the specific health packages
    sp_hp = HealthPackages.objects.filter(MainPackage = id)

    return render(request, template_name, {'hp': hp, 'sp_hp': sp_hp})


def sp_health_packagess(request, id):
    template_name = 'extras/sp_health_package.html'
    hp_details = HealthPackages.objects.get(id=id)
    main_p = HealthPackageMain.objects.get(id = hp_details.MainPackage.id)
    return render(request, template_name, {'hp_details': hp_details, 'main_p': main_p})