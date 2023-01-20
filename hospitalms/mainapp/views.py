from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomRCreationForm, CustomDCreationForm, CustomPCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
from .models import CustomUser, Receptionist, Doctor, Patient, Appointments, ReviewComment
from mainapp.forms import UserUpdateForm, CustomUserUpdateForm, CustomRUserUpdateForm, CustomDUserUpdateForm, CustomPUserUpdateForm, AppointmentForm, ReviewCommentForm
from datetime import datetime


def index(request):
    """ Home Page """
    template_name = 'mainapp/landing-page.html'
    return render(request, template_name)

def user_login(request):
    template_name = 'mainapp/user_login.html'
    if  request.user.is_authenticated:
        return redirect('mainapp:index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainapp:index')
        
        else:
            messages.success(request, ("The login was failed."))
            return redirect('mainapp:user_login')
        
    else:
        return render(request, template_name)

def signupview(request):
    """ create new users """
    if request.user.is_authenticated:
        return redirect('mainapp:index')
    form = CustomUserCreationForm(request.POST or None)
    # r_form = CustomRCreationForm(request.POST or None)
    # d_form = CustomDCreationForm(request.POST or None)
    # p_form = CustomPCreationForm(request.POST or None)

    if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('mainapp:index')
            else:
                print(form.errors)
                messages.success(request, ("The login was failed."))
                form = CustomUserCreationForm()
    return render(request, 'mainapp/register.html', {'form': form, 'title':'Register here'})


def profileview(request):
    template_name = 'mainapp/profile.html'
    return render(request, template_name)

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'mainapp/password-change.html'
    # success_url = reverse_lazy('password-change-done-view')
    success_url = reverse_lazy('mainapp:index')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'mainapp/password_reset_complete.html'


def logout_view(request):
    logout(request)
    return redirect('/')


def update_information(request):
    """ Update basic information of users """
    template_name = 'mainapp/update_information.html'

    if request.method == "POST":
        myuser = CustomUser.objects.get(id = request.user.id )

        user_form = UserUpdateForm(request.POST, instance = request.user)
        custom_user_form = CustomUserUpdateForm(request.POST, instance = myuser)


        if user_form.is_valid() and custom_user_form.is_valid():
            user_form.save()
            custom_user_form.save()
            return redirect('/')

    else:
        myuser = CustomUser.objects.get(id = request.user.id )

        user_form = UserUpdateForm(instance = request.user)
        custom_user_form = CustomUserUpdateForm(instance = myuser)
        
    role = str(request.user.role)
    context = {
        'user_form': user_form,
        'custom_user_form': custom_user_form,
        'role': role,
    }
    return render(request, template_name, context)

def complete_information_staff(request):
    template_name = 'mainapp/complete_information_staff.html'
    staff_list = Receptionist.objects.all()
    user_status = 0
    for j in staff_list:
        if j.User == request.user:
            user_status=1
    
    if user_status == 0 and request.method == "POST":
        r_user = Receptionist.objects.create(User=request.user, staff_number = request.POST.get('staff_number'))
        r_user.save()
        return redirect('/')
    if user_status == 1 and request.method == "POST":
        myuser = CustomUser.objects.get(id = request.user.id )
        r_user = Receptionist.objects.get(User=myuser)

        r_user_form = CustomRUserUpdateForm(request.POST, instance = r_user)


        if r_user_form.is_valid():
            r_user_form.save()
            return redirect('/')

    elif user_status == 0 and request.method== "GET":
        r_user_form = ''
    else:
        myuser = CustomUser.objects.get(id = request.user.id )
        
        r_user = Receptionist.objects.get(User=myuser)
        r_user_form = CustomRUserUpdateForm(instance = r_user)
        print('r_user_form')
        print(r_user_form)

    return render(request, template_name, {'user_status': user_status, 'r_user_form': r_user_form})


def complete_information_doctor(request):
    template_name = 'mainapp/complete_information_doctor.html'
    doctor_list = Doctor.objects.all()
    user_status = 0
    for j in doctor_list:
        if j.User == request.user:
            user_status=1
    
    if user_status == 0 and request.method == "POST":
        d_user = Doctor.objects.create(User=request.user, specialization = request.POST.get('specialization'), availability =  request.POST.get('avialable'), doctor_image =  request.FILES.get('image'))
        d_user.save()
        return redirect('/')
    if user_status == 1 and request.method == "POST":
        myuser = CustomUser.objects.get(id = request.user.id )
        d_user = Doctor.objects.get(User=myuser)

        d_user_form = CustomDUserUpdateForm(request.POST, request.FILES, instance = d_user)
        print("d_user_form1:")
        print(d_user_form)

        if d_user_form.is_valid():
            print('d_user_form2')
            print(d_user_form)
            d_user_form.save()
            return redirect('/')

    elif user_status == 0 and request.method== "GET":
        d_user_form = ''
    else:
        myuser = CustomUser.objects.get(id = request.user.id )
        
        d_user = Doctor.objects.get(User=myuser)
        d_user_form = CustomDUserUpdateForm(instance = d_user)
        # print('d_user_form')
        # print(d_user_form)

    return render(request, template_name, {'user_status': user_status, 'd_user_form': d_user_form})


def complete_information_patient(request):
    template_name = 'mainapp/complete_information_patient.html'
    patient_list = Patient.objects.all()
    user_status = 0
    for j  in patient_list:
        if j.User == request.user:
            user_status=1
     
    if user_status == 0 and request.method == "POST":
        p_user = Patient.objects.create(User=request.user, address = request.POST.get('address'))
        p_user.save()
        return redirect('/')
    
    if user_status == 1 and request.method == "POST":
        myuser = CustomUser.objects.get(id = request.user.id )
        p_user = Patient.objects.get(User=myuser)

        p_user_form = CustomPUserUpdateForm(request.POST, instance = p_user)


        if p_user_form.is_valid():
            p_user_form.save()
            return redirect('/')
    elif user_status == 0 and request.method== "GET":
        p_user_form = ''
    else:
        myuser = CustomUser.objects.get(id = request.user.id )

        p_user = Patient.objects.get(User=myuser)
        p_user_form = CustomPUserUpdateForm(instance = p_user)
        print('p_user_form')
        print(p_user_form)

    return render(request, template_name, {'user_status': user_status, 'p_user_form': p_user_form})

def doctors_specialization_view(request):
    """ List all the doctors categoryies or specialization for the appointment """
    template_name = 'mainapp/view_doctors_specialization.html'

    doctor_users = CustomUser.objects.filter(role=3)
    print('doctor_users')
    print(doctor_users)
    return render(request, template_name)


def doctors_view_details(request, id):
    """ The details page of all the doctors where the user can book an appointment with the doctor """
    template_name = 'mainapp/doctor-details.html'
    
    doctor_data = Doctor.objects.get(id=id)
    user_data = CustomUser.objects.get(id = doctor_data.User.id)

    if request.method == 'POST':
        user = request.user
        form = AppointmentForm(request.POST)
        appointment_date_from_user =  request.POST['appointment_date']
        present = datetime.now()
       
        if form.is_valid():

                if appointment_date_from_user < str(present.date()):
                    messages.warning(request, ("The Appointment date was Old."))
                    return redirect('/doctors-view-details/'+str(id))
                    
                else:
                    form.save(commit=False)
                    form.doctor = id
                    form.booked_by = request.user
                    form.save()
                    messages.success(request, ("The Appointment was Booked."))

                    return redirect('/doctors-view-details/'+str(id))
        else:
            print(form.errors)
            messages.warning(request, 'The Appointment was failed.')
            form = AppointmentForm()
            errors = form.errors
            user = request.user

    else:
        form = AppointmentForm()
        errors = ''
        user = request.user
   
    return render(request, template_name, {'doctor_data': doctor_data, 'user': user, 'user_data': user_data, 'errors': errors, 'appointment_form': form})

# Users can review and comment the doctors

def review_and_comment(request, id):
    template_name = 'mainapp/review_and_comment.html'
    doctor_data = Doctor.objects.get(id=id)
    patient = CustomUser.objects.get(id=request.user.id)
    reviews_comments = ReviewComment.objects.all()
    print(reviews_comments)
    doctor_specific_comments = ReviewComment.objects.filter(doctor=id).order_by("-review_date")

    print('doctor_specific_comments')
    print(doctor_specific_comments)
    if request.method == 'POST':
        commenting_user =  request.user
        form = ReviewCommentForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            form.doctor = id
            form.patient = commenting_user
            form.save()
            messages.success(request, "Commented Successfully")

            return redirect('/review_and_comments/'+str(id))
        else:
            print(form.errors)
            messages.warning(request, 'The Appointment was failed.')
            form = AppointmentForm()
    else:
        form =  ReviewCommentForm()
        user = request.user
    return render(request, template_name, {'form': form, 'doctor_data': doctor_data, 'patient': patient, 'doctor_specific_comments': doctor_specific_comments})


# Users can view the appointments boked by them

def view_appointments(request, id):
    template_name = 'mainapp/view_appointmentss.html'
    logged_in_user = CustomUser.objects.get(id = id)
    print(type(logged_in_user.role))
    print(logged_in_user)
    if str(logged_in_user.role) != 'Doctor':
        appointments = Appointments.objects.filter(booked_by=id) 
        print('Rolle != 3')
        print(appointments)
        role_my = ''
    else:
        appointments = Appointments.objects.filter(doctor = id)
        role_my = 'Doctor'
        print('appointment by doctor')
        print(appointments)
    present = datetime.now()
    send_present = str(present)
    return render(request, template_name, {'appointments': appointments, 'send_present': send_present, 'role_my': role_my})

# User can cancel or delete the appointments made by them

def delete_appointments(request, id):
    appointment_to_delete = Appointments.objects.get(id=id)
    appointment_to_delete.delete()
    appointments = Appointments.objects.filter(booked_by=request.user.id) 

    return render(request, 'mainapp/view_appointmentss.html',{'appointments': appointments})

# Users can delete their comments

def delete_comments(request, id):
    comment_to_delete = ReviewComment.objects.get(id=id)
    comment_to_delete.delete()
    doctor_specific_comments = ReviewComment.objects.filter(doctor=comment_to_delete.doctor.id).order_by("-review_date")
    form =  ReviewCommentForm()
    doctor_data = Doctor.objects.get(id=comment_to_delete.doctor.id)
    patient = CustomUser.objects.get(id=request.user.id)

    return render(request, 'mainapp/review_and_comment.html', {'form': form, 'doctor_data': doctor_data, 'patient': patient, 'doctor_specific_comments': doctor_specific_comments} )
# This is the series of views for various doctor specialization

def doctors_view_gc(request):
    """ List all the doctors registered for the appointment (General Clinics) """
    
    template_name = "mainapp/specialization/gc_doctors.html"

    doctors = Doctor.objects.filter(specialization="General Clinics")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_ayurveda(request):
    """ List all the doctors registered for the appointment (Ayurveda Specialists) """
    
    template_name = "mainapp/specialization/ayurveda.html"

    doctors = Doctor.objects.filter(specialization="Ayurveda Specialists")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_cancer(request):
    """ List all the doctors registered for the appointment (Cancer Specialists) """
    
    template_name = "mainapp/specialization/cancer_doctors.html"

    doctors = Doctor.objects.filter(specialization="Cancer Specialists")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_child(request):
    """ List all the doctors registered for the appointment (Child Specialists) """
    
    template_name = "mainapp/specialization/child.html"

    doctors = Doctor.objects.filter(specialization="Child Health")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_dental(request):
    """ List all the doctors registered for the appointment (Dental Specialists) """
    
    template_name = "mainapp/specialization/dental.html"

    doctors = Doctor.objects.filter(specialization="Dental Cares")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_diet(request):
    """ List all the doctors registered for the appointment (Diet Specialists) """
    
    template_name = "mainapp/specialization/diet.html"

    doctors = Doctor.objects.filter(specialization="Diet and Nutrition")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_dth(request):
    """ List all the doctors registered for the appointment (DTH Specialists) """
    
    template_name = "mainapp/specialization/dth.html"

    doctors = Doctor.objects.filter(specialization="Diabetes, Thyroid and Hormonal")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_ent(request):
    """ List all the doctors registered for the appointment (ENT Specialists) """
    
    template_name = "mainapp/specialization/ent.html"

    doctors = Doctor.objects.filter(specialization="ENT specialists")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_kidney(request):
    """ List all the doctors registered for the appointment (Kidney Specialists) """
    
    template_name = "mainapp/specialization/kidney.html"

    doctors = Doctor.objects.filter(specialization="Kidney Specialists")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_mh(request):
    """ List all the doctors registered for the appointment (Mental Health) """
    
    template_name = "mainapp/specialization/mh_doctors.html"

    doctors = Doctor.objects.filter(specialization="Mental Health")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_physio(request):
    """ List all the doctors registered for the appointment (Physiotherapy Centers) """
    
    template_name = "mainapp/specialization/physio.html"

    doctors = Doctor.objects.filter(specialization="Physiotherapy Centers")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})


def doctors_view_pregnancy(request):
    """ List all the doctors registered for the appointment (Pregnancy Centers) """
    
    template_name = "mainapp/specialization/pregnancy.html"

    doctors = Doctor.objects.filter(specialization="Pregnancy and Infertility")
    print('doctors_gc')
    print(doctors)

    return render(request, template_name, {'doctors': doctors})