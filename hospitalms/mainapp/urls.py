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

]