from django.urls import path

from .views import index, signupview, profileview, user_login,MyPasswordChangeView, MyPasswordResetDoneView
from . import views

app_name='mainapp'
urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('register/', signupview, name='signup'),
    path('profile/', profileview, name='profile'),
    path('password-change/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('password-change-done/', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('update_information/', views.update_information, name='update_information'),
    path('complete-information-staff/', views.complete_information_staff, name='complete_information_staff'),
    path('complete-information-doctor/', views.complete_information_doctor, name='complete_information_doctor'),
    path('complete-information-patient/', views.complete_information_patient, name='complete_information_patient'),
    
    path('doctors-specialization-listing', views.doctors_specialization_view, name='doctors_specialization_view'),
    path('doctors-view-gc', views.doctors_view_gc, name='doctors_view_gc'),
    path('doctors-view-ayurveda', views.doctors_view_ayurveda, name='doctors_view_ayurveda'),
    path('doctors-view-cancer', views.doctors_view_cancer, name='doctors_view_cancer'),
    path('doctors-view-child', views.doctors_view_child, name='doctors_view_child'),
    path('doctors-view-dental', views.doctors_view_dental, name='doctors_view_dental'),
    path('doctors-view-diet', views.doctors_view_diet, name='doctors_view_diet'),
    path('doctors-view-dth', views.doctors_view_dth, name='doctors_view_dth'),
    path('doctors-view-ent', views.doctors_view_ent, name='doctors_view_ent'),
    path('doctors-view-kidney', views.doctors_view_kidney, name='doctors_view_kidney'),
    path('doctors-view-mh', views.doctors_view_mh, name='doctors_view_mh'),
    path('doctors-view-physio', views.doctors_view_physio, name='doctors_view_physio'),
    path('doctors-view-pregnancy', views.doctors_view_pregnancy, name='doctors_view_pregnancy'),

    # details page to books the particular doctor
    path('doctors-view-details/<int:id>', views.doctors_view_details, name='doctors_view_details'),

    # User can view their booked appointments
    path('view_appointmentss/<int:id>', views.view_appointments, name='view_appointments'),

    # User can delete the booked appointments
    path('delete_appointment/<int:id>', views.delete_appointments, name='delete_appointments'),
    
    #Users can review and comment the doctor
    path('review_and_comments/<int:id>', views.review_and_comment, name='review_and_comment'),

    #Users can delete their comments
    path('delete_comments/<int:id>', views.delete_comments, name='delete_comments'),


]