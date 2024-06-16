from django.urls import path
from .views import login_member, login_admin, reset_password, send_reset_code, logout_user, change_password, register_member


urlpatterns = [
    path('login-member/', login_member, name='login-member'),
    path('login-admin/', login_admin, name='login-admin'),
    path('reset-password/', reset_password, name='reset-password'),
    path('send-reset-code/', send_reset_code, name='send-reset-code'),
    path('change-password/', change_password, name='change-password'),
    path('register-member/<registration_code>/', register_member, name='register-member'),
    path('logout/', logout_user, name='logout'),
]