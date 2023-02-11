from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.forms.widgets import Textarea
from .models import CustomUser, Receptionist, Doctor, Patient, Appointments, ReviewComment
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

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointments
        fields = ['doctor', 'booked_by', 'appointment_date','appointment_time','message']
        widgets = {
            'appointment_date': DateInput(),
            'appointment_time': TimeInput(),
        }


class ReviewCommentForm(forms.ModelForm):

    class Meta:
        model = ReviewComment
        fields = '__all__'

"""""""""" Updating forms"""""""""""

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone']

class CustomRUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ['staff_number']

class CustomDUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'availability', 'doctor_image']

class CustomPUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address']