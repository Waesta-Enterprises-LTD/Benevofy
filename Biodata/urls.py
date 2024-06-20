from django.urls import path
from . import views

urlpatterns = [
    path('biodata/', views.biodata, name='biodata'),
    path('add-biodata/', views.add_biodata, name='add_biodata'),
    path('view-dependents/', views.view_dependents, name='view_dependents'),
    path('add-dependent/', views.add_dependent, name='add_dependent'),
    path('member-dependents/<int:member_id>/', views.member_dependents, name='member_dependents'),
    path('edit-dependent/<int:dependent_id>/', views.edit_dependent, name='edit_dependent'),
]