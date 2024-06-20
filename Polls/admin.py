from django.db import models
from django.contrib import admin
from .models import Poll, Candidate, Constitution, ConstitutionalVote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'closing_date', 'status', 'poll_type']
    


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(Constitution)
class ConstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(ConstitutionalVote)
class ConstitutionalVoteAdmin(admin.ModelAdmin):
    pass

