from django.shortcuts import render, redirect
from .models import Candidate, Poll
from .forms import PollForm, CandidateForm
from Members.models import Member


def create_poll(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST)  
        if form.is_valid():
            form.instance.association = request.user.member.logged_in_association
            form.save()
            return render(request, 'benevofy/create_poll.html', {'form': form})
    return render(request, 'benevofy/create_poll.html', {'form': form})


def add_candidate(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    form = CandidateForm()
    members = Member.objects.exclude(id__in=poll.candidates.all().values_list('id', flat=True))
    form = CandidateForm()
    form.fields['member'].queryset = members
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate, created = Candidate.objects.get_or_create(
                member=form.cleaned_data['member'],
            )
            if created:
                candidate.save()
            poll.candidates.add(candidate)
            return redirect('polls')
    return render(request, 'benevofy/add_candidate.html', {'form': form, 'poll': poll})


def disqualify_candidate(request, poll_id, candidate_id):
    poll = Poll.objects.get(pk=poll_id)
    candidate = Candidate.objects.get(pk=candidate_id)
    poll.candidates.remove(candidate)
    return redirect('polls')

def delete_poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    poll.delete()
    return render(request, 'benevofy/delete_poll.html', {'poll': poll})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, poll_id):
    member = request.user.member
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'benevofy/vote.html', {'member': member, 'poll': poll})


def view_polls(request):
    polls = Poll.objects.all()
    return render(request, 'benevofy/view_polls.html', {'polls': polls})
