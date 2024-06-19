from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('Auth/', include('Auth.urls')),
    path('Administrators/', include('Administrators.urls')),
    path('Associations/', include('Associations.urls')),
    path('Events/', include('Events.urls')),
    path('LoanRequests/', include('LoanRequests.urls')),
    path('Loans/', include('Loans.urls')),
    path('Members/', include('Members.urls')),
    path('Payments/', include('Payments.urls')),
    path('Contributions/', include('Contributions.urls')),
    path('Savings/', include('Savings.urls')),
    path('Polls/', include('Polls.urls')),
    path('Biodata/', include('Biodata.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

