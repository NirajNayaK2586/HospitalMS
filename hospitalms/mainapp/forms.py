from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.forms.widgets import Textarea
from .models import CustomUser, Receptionist, Doctor, Patient
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role']

        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'

class CustomRCreationForm(forms.ModelForm):

    class Meta:
        model = Receptionist
        fields = ['staff_number']

class CustomDCreationForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['specialization', 'availability']

class CustomPCreationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['address']


"""""""""" Updating forms"""""""""""

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone']

class CustomRUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ['staff_number']

class CustomDUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'availability']

class CustomPUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address']