from django.urls import path
from .views import login_member, login_admin, reset_password, send_reset_code, logout_user, change_password, register_member, verify_email, switch_association, switch_to_admin, switch_to_member, register_exists, switch_to_personal_account


urlpatterns = [
    path('login-member/', login_member, name='login-member'),
    path('login-admin/', login_admin, name='login-admin'),
    path('reset-password/', reset_password, name='reset-password'),
    path('send-reset-code/', send_reset_code, name='send-reset-code'),
    path('change-password/', change_password, name='change-password'),
    path('register-member/<registration_code>/', register_member, name='register-member'),
    path('verify-email/<verification_code>/', verify_email, name='verify-email'),
    path('switch-association/<int:association_id>/', switch_association, name='switch-association'),
    path('switch-to-member/', switch_to_member, name='switch-to-member'),
    path('switch-to-admin/', switch_to_admin, name='switch-to-admin'),
    path('register-exists/', register_exists, name='register-exists'),
    path('switch-to-personal-account/', switch_to_personal_account, name='switch-to-personal-account'),
    path('logout/', logout_user, name='logout'),
]