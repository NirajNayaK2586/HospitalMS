from django.shortcuts import render, redirect
from .models import HealthPackageMain, HealthPackages, ChildCare
from mainapp.models import CustomUser, Patient, Bills
from django.contrib import messages
from .forms import BillsForm
import datetime

# PDF

import io
from django.core.files.base import ContentFile
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth.decorators import login_required


def health_packages(request):
    template_name = 'extras/health_packages.html'
    hpmain = HealthPackageMain.objects.all()

    return render(request, template_name, {'hpmains': hpmain})


def health_packagess(request, id):
    template_name = 'extras/health_packagess_list.html'

    hp = HealthPackageMain.objects.get(id=id)
    # Save the specific health packages
    sp_hp = HealthPackages.objects.filter(MainPackage=id)

    return render(request, template_name, {'hp': hp, 'sp_hp': sp_hp})


def childcare(request):
    template_name = 'extras/childcare.html'
    cc = ChildCare.objects.all()
    return render(request, template_name, {'cc': cc})


def childcaredetails(request, id):
    template_name = 'extras/childcaredetails.html'
    ccdetails = ChildCare.objects.get(id=id)
    return render(request, template_name, {'ccdetail': ccdetails})

def sp_health_packagess(request, id):
    template_name = 'extras/sp_health_package.html'
    hp_details = HealthPackages.objects.get(id=id)
    main_p = HealthPackageMain.objects.get(id=hp_details.MainPackage.id)
    user = request.user
    string_user = str(user)
    if string_user == 'AnonymousUser':
        role = ''
    else:
        role = str(user.role)
    print('role')
    print(role)
    return render(request, template_name, {'role': role, 'hp_details': hp_details, 'main_p': main_p})

def buy_package(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        template_name = 'extras/buy_package.html'

        health_package = HealthPackages.objects.get(id=id)
        user = CustomUser.objects.get(id=request.user.id)
        role = user.role
        current_datetime = datetime.datetime.now()

        patient_information = Patient.objects.get(User=user)
        main_p = HealthPackageMain.objects.get(id=health_package.MainPackage.id)

        already_purchased = 0
        for bill in Bills.objects.filter(patient=patient_information.id):
            print('bill')
            print(bill.package)
            if bill.package == health_package:
                already_purchased = 1

        if request.method == 'POST':
            form = BillsForm(request.POST)
            package = request.POST['package']
            patient = request.POST['patient']

            print("Before Valid testing")
            print("package")
            print(package)
            print("patient")
            print(patient)

            if form.is_valid():
                print(form)
                form.save(commit=False)
                bill_title = 'Bill-' + health_package.package_title + '-' + \
                    patient_information.User.username + ':' + form.instance.payment_method
                form.instance.bill_title = bill_title

                # PDF
                # Bytestream buffer
                buf = io.BytesIO()

                # Canvas
                c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

                # Text

                textob = c.beginText()
                textob.setTextOrigin(inch, inch)
                textob.setFont("Helvetica", 18)

                # lines
                lines = [
                    "HospitalMS Bill",
                    "",
                    "",
                    health_package.package_title,
                    "",
                    "Bill Info: #" + bill_title,
                    "Issued Date: " + str(current_datetime),
                    "",
                    "Username : " + user.username,
                    "Email : " + user.email,
                    "Patient Phone : " + user.phone,
                    "Patient First Name : " + user.first_name,
                    "Patient Last Name : " + user.last_name,
                    "Patient Address : " + patient_information.address,
                    " ",
                    "----------------------------------------------------------------------------",
                    "",
                    "Package Information",
                    "",
                    "Total Tests : " + str(health_package.total_tests),
                    "Package Category : " + main_p.package_title_main,
                    " ",
                    " ",
                    "....................................................................................",

                    "Bill amount  Rs." + str(health_package.package_price),
                    " ",
                    " ",
                    "Status : Unpaid - " + form.instance.payment_method,
                ]

                for line in lines:
                    textob.textLine(line)

                # Finsihsit

                c.drawText(textob)
                c.showPage()
                c.save()
                buf.seek(0)
                print('c')
                print(c)
                print(buf)

                pdf = buf.getvalue()

                print('pdf')
                print(pdf)

                file_data = ContentFile(pdf)
                file_data.name = 'test.pdf'
                print('file_data')
                print(file_data.name)
                form.instance.bill = file_data

                order = form.save()
                bilkoid = form.instance.id
                messages.success(request, ("The package has been bought."))
                if form.instance.payment_method == 'Cash On Delivery':
                    # return FileResponse(buf, as_attachment=True, filename='bill.pdf')
                    return redirect('/extras/verify_bill/'+str(bilkoid))
                else:
                    return redirect('/extras/khalti_verify_bill/' + str(order.id))
            else:
                print(form.errors)
                messages.warning(request, 'The Buying was failed.')
                form = BillsForm()
                errors = form.errors
                user = request.user
        else:
            form = BillsForm()
            user = request.user
        return render(request, template_name, {'already_purchased': already_purchased, 'health_package': health_package, 'form': form, 'user': user, 'patient_information': patient_information, 'role': role, 'main_p': main_p})


def verify_bill(request, id):
    template_name = 'extras/verify_bill.html'
    bill = Bills.objects.get(id=id)

    return render(request, template_name, {'bill': bill})


def khalti_verify_bill(request, id):
    template_name = 'extras/khalti_verify_bill.html'
    # o_id = request.GET.get("o_id")
    order = Bills.objects.get(id=id)
    package_orderd = HealthPackages.objects.get(id=order.package.id)
    context = {
        "order": order,
        "package_orderd": package_orderd,
    }

    return render(request, template_name, context)


def about(request):
    template_name = 'extras/about.html'

    return render(request, template_name)
