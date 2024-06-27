from django.urls import path
from .views import view_withdraws, make_withdraw, reject_withdraw, approve_withdraw, cancel_withdraw


urlpatterns = [
    path('view_withdraws/', view_withdraws, name='view_withdraws'),
    path('make_withdraw/', make_withdraw, name='make_withdraw'),
    path('reject_withdraw/<int:withdraw_id>/', reject_withdraw, name='reject_withdraw'),
    path('approve_withdraw/<int:withdraw_id>/', approve_withdraw, name='approve_withdraw'),
    path('cancel_withdraw/<int:withdraw_id>/', cancel_withdraw, name='cancel_withdraw'),
]