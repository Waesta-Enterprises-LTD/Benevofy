from django.shortcuts import render, redirect
from .models import Candidate, Poll
from .forms import PollForm, CandidateForm, ConstitutionForm
from Members.models import Member


def create_poll(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST)  
        if form.is_valid():
            form.instance.association = request.user.member.logged_in_association
            form.save()
            return redirect('polls')
    return render(request, 'benevofy/create_poll.html', {'form': form})


def add_candidate(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    form = CandidateForm()
    members = Member.objects.exclude(id__in=poll.candidates.all().values_list('id', flat=True), associations=request.user.member.logged_in_association)
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
    return redirect('polls')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, poll_id):
    member = request.user.member
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'benevofy/vote.html', {'member': member, 'poll': poll})


def vote_candidate(request, poll_id, candidate_id):
    poll = Poll.objects.get(pk=poll_id)
    candidate = poll.candidates.get(pk=candidate_id)
    candidate.votes.add(request.user.member)
    poll.voters.add(request.user.member)
    return redirect('thanks_for_voting', poll_id, candidate_id)


def vote_constitution(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        constitution = poll.constitution
        constitution.votes.create(
            member=request.user.member,
            poll=poll,
            vote=request.POST.get('vote'),
        )
        poll.voters.add(request.user.member)
        return redirect('thanks_for_voting', poll_id, constitution.id)
    return render(request, 'benevofy/vote_constitution.html', {'poll': poll})


def thanks_for_voting(request, poll_id, candidate_id):
    poll = Poll.objects.get(pk=poll_id)
    if poll.poll_type == 'Electoral':
        candidate = poll.candidates.get(pk=candidate_id)
        return render(request, 'benevofy/thanks_for_voting.html', {'poll': poll, 'candidate': candidate})
    else:
        constitution = poll.constitution
        return render(request, 'benevofy/thanks_for_voting.html', {'poll': poll, 'constitution': constitution})
    


def view_polls(request):
    polls = Poll.objects.filter(association=request.user.member.logged_in_association)
    return render(request, 'benevofy/view_polls.html', {'polls': polls})


def view_poll_results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if poll.poll_type == 'Constitutional':
        yes = poll.constitution.votes.filter(vote='Yes').count()
        no = poll.constitution.votes.filter(vote='No').count()
        neutral = poll.constitution.votes.filter(vote='Neutral').count()
        return render(request, 'benevofy/view_poll_results.html', {'poll': poll, 'yes': yes, 'no': no, 'neutral': neutral})
    return render(request, 'benevofy/view_poll_results.html', {'poll': poll})


def write_constitution(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    form = ConstitutionForm()
    if request.method == 'POST':
        form = ConstitutionForm(request.POST)
        if form.is_valid():
            constitution = form.save(commit=False)
            constitution.poll = poll
            constitution.save()
            poll.constitution = constitution
            poll.save()
            return redirect('polls')
    return render(request, 'benevofy/write_constitution.html', {'form': form, 'poll': poll})