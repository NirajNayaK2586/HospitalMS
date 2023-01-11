from django.db import models
from django.contrib.auth.models import AbstractUser

''' Model to store the roles of a user '''
class Role(models.Model):
    role_name = models.CharField(max_length=25)

    def __str__(self):
        return self.role_name

''' A base class for the users '''
class CustomUser(AbstractUser):
    # customizing fields
    email = models.EmailField(verbose_name='email',max_length=100, unique=True,)
    phone = models.CharField(max_length=10)                            
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=4)

    # here, email is already a required field
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username


''' A class unique to Receptionists '''
class Receptionist(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    staff_number = models.IntegerField()
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.User.email



''' A class unique to Doctors  '''
class Doctor(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    availability = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.User.email


''' A class unique to Patients '''
class Patient(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.User.email


''' A class to store appointments '''
class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(Patient, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now=True)
    appointment_time = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.appointment_time

''' A class to store reports '''
class Report(models.Model):
    report_title = models.CharField(max_length=50)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    report = models.FileField(upload_to='report_file')

    def __str__(self):
        return self.report_title

''' Comment and review model'''
class ReviewComment(models.Model):
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now=True)
    review_rating = models.IntegerField()
    review_comment = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doctor)


''' Bills model '''
class Bills(models.Model):
    bill_title = models.CharField(max_length=50)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    bill = models.FileField(upload_to='bills_file')
    
    def __str__(self):
        return self.bill_title



