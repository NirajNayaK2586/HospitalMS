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
    specialization_choices = (
        ('General Clinics', 'General Clinics'),
        ('Mental Health', 'Mental Health'),
        ('Eye Specialists', 'Eye Specialists'),
        ('Cancer Specialists', 'Cancer Specialists'),
        ('Ayurveda Specialists', 'Ayurveda Specialists'),
        ('ENT specialists', 'ENT specialists'),
        ('Skin, Sex and Hair', 'Skin, Sex and Hair'),
        ('Child Health', 'Child Health'),
        ('Diabetes, Thyroid and Hormonal', 'Diabetes, Thyroid and Hormonal'),
        ('Pregnancy and Infertility', 'Pregnancy and Infertility'),
        ('Kidney Specialists', 'Kidney Specialists'),
        ('Dental Cares', 'Dental Cares'),
        ('Physiotherapy Centers', 'Physiotherapy Centers'),
        ('Diet and Nutrition', 'Diet and Nutrition'),

    ) 
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(choices=specialization_choices, max_length=120, default='General Clinics')
    availability = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)
    short_description = models.TextField(default="Specialist Doctor",blank=True)
    doctor_image = models.ImageField(upload_to='doctors_image', blank=True)

    def __str__(self):
        return self.User.username


''' A class unique to Patients '''
class Patient(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.User.username


''' A class to store appointments '''
class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField()
    status = models.BooleanField(default=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.booked_by.username

''' A class to store reports '''
class Report(models.Model):
    report_title = models.CharField(max_length=50)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    report = models.FileField(upload_to='report_file')
    doctor_review = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now=True, null=True)
    # I could link the appointment if necessary later
    def __str__(self):
        return '%s %s %s' % (self.report_title,self.patient, self.doctor)

''' Comment and review model'''
class ReviewComment(models.Model):
    patient =models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now=True)
    review_rating = models.IntegerField()
    review_comment = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.doctor,self.patient)


''' Bills model '''
class Bills(models.Model):
    METHOD = (
        ("Cash On Delivery", "Cash On Delivery"),
        ("Khalti", "Khalti"),
    )
    bill_title = models.CharField(max_length=50)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    bill = models.FileField(upload_to='bills_file')
    paid = models.BooleanField(default=False, null=True, blank=True)
    payment_method = models.CharField(max_length=50, choices=METHOD, default = "Cash On Delivery")
   
    def __str__(self):
        return self.bill_title



