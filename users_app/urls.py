from django.urls import path
from users_app import views
from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login_doctor', auth_views.LoginView.as_view(template_name='login_doctor.html'), name='login_doctor'),
    path('logout_doctor', auth_views.LogoutView.as_view(template_name='logout_doctor.html'), name='logout_doctor'),
    path('login_secretary', auth_views.LoginView.as_view(template_name='login_secretary.html'), name='login_secretary'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    
]