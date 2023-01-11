from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomRCreationForm, CustomDCreationForm, CustomPCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
from .models import CustomUser, Receptionist, Doctor, Patient
from mainapp.forms import UserUpdateForm, CustomUserUpdateForm, CustomRUserUpdateForm, CustomDUserUpdateForm, CustomPUserUpdateForm

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
        d_user = Doctor.objects.create(User=request.user, specialization = request.POST.get('specialization'), availability =  request.POST.get('avialable'))
        d_user.save()
        return redirect('/')
    if user_status == 1 and request.method == "POST":
        myuser = CustomUser.objects.get(id = request.user.id )
        d_user = Doctor.objects.get(User=myuser)

        d_user_form = CustomDUserUpdateForm(request.POST, instance = d_user)
        print("d_user_form:")

        if d_user_form.is_valid():
            d_user_form.save()
            return redirect('/')

    elif user_status == 0 and request.method== "GET":
        d_user_form = ''
    else:
        myuser = CustomUser.objects.get(id = request.user.id )
        
        d_user = Doctor.objects.get(User=myuser)
        d_user_form = CustomDUserUpdateForm(instance = d_user)
        print('d_user_form')
        print(d_user_form)

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