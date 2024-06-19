from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('create_poll/', views.create_poll, name='create-poll'),
    path('delete_poll/<int:poll_id>/', views.delete_poll, name='delete-poll'),
    path('add_candidate/<int:poll_id>/', views.add_candidate, name='add_candidate'),
    path('disqualify_candidate/<int:poll_id>/<int:candidate_id>/', views.disqualify_candidate, name='disqualify_candidate'),
    path('view_polls/', views.view_polls, name='polls'),
    path('vote_candidate/<int:poll_id>/<int:candidate_id>/', views.vote_candidate, name='vote_candidate'),
    path('thanks_for_voting/<int:poll_id>/<int:candidate_id>/', views.thanks_for_voting, name='thanks_for_voting'),
    path('view_poll_results/<int:poll_id>/', views.view_poll_results, name='view_poll_results'),
    path('write_constitution/<int:poll_id>/', views.write_constitution, name='write_constitution'),
    path('vote_constitution/<int:poll_id>/', views.vote_constitution, name='vote_constitution'),
]

