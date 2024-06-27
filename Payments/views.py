from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from Contributions.models import EventContribution, PersonalEventContribution
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Events.models import Event, PersonalEvent
from Savings.models import Saving
from Loans.models import LoanRepayment
from .models import Payment, RegistrationPayment
from uuid import uuid4
from django.db.models import Q


def payment_initiated(request):
    if request.user.is_authenticated:
        return render(request, 'benevofy/payment_initiated.html')
    else:
        return render(request, 'benevofy/payment_init.html')


@csrf_exempt
@require_http_methods(['POST'])
def webhook_receiver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            contribution = PersonalEventContribution.objects.get(reference=data['customer_reference'])
            if data['status'] == 'success':
                contribution.status = 'Paid'
                contribution.save()
            else:
                contribution.delete()
        except PersonalEventContribution.DoesNotExist:
            pass
        try:
            registration = RegistrationPayment.objects.get(reference=data['customer_reference'])
            if data['status'] == 'success':
                registration.association.registration_code = str(uuid4())
                registration.association.save()
                registration.status = 'Paid'
                registration.save()
                registration.association.members.add(registration.user)
                registration.user.associations.add(registration.association)
                registration.user.current_mode = 'Member'
                registration.user.logged_in_association = registration.association
                registration.user.save()
            else:
                registration.delete()
        except RegistrationPayment.DoesNotExist:
            pass
        contributions = EventContribution.objects.filter(reference=data['customer_reference'])
        if contributions.count() == 0:
            savings = Saving.objects.filter(reference=data['customer_reference'])
            if savings.count() == 0:
                loan_repayment = LoanRepayment.objects.filter(reference=data['customer_reference'])
                if data['status'] == 'success':
                    loan_repayment.update(status='Paid')
                else:
                    loan_repayment.delete()
            else:
                if data['status'] == 'success':
                    savings.update(status='Paid')
                else:
                    savings.delete()
        else:
            if data['status'] == 'success':
                contributions.update(status='Paid')
                for contribution in contributions:
                    contribution.event.contributions.add(contribution)
            else:
                contributions.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
                


def view_paid_list(request, event_id):
    event = Event.objects.get(pk=event_id)
    contributions = EventContribution.objects.filter(event=event, status='Paid').order_by('-created_at')
    members = request.user.member.logged_in_association.members.exclude(id__in=contributions.values_list('user_id', flat=True)).distinct()
    return render(request, 'benevofy/view_paid_list.html', {'contributions': contributions, 'event': event, 'members': members})


def add_manual_payment(request, event_id):
    if request.method == 'POST':
        member = request.user.member
        event = Event.objects.get(pk=event_id)
        member_paid = request.POST.get('member')
        currency = request.POST.get('currency')
        member_paid = member.logged_in_association.members.get(id=member_paid)
        amount = request.POST.get('amount')
        reference = str(uuid4())
        contribution = EventContribution.objects.create(
            user=member_paid,
            event=event,
            reference=reference,
            amount=amount,
            method='Manual',
            currency=currency,
            status='Paid'
        )
        member_paid.contributions.add(contribution)
        event.contributions.add(contribution)
        return redirect('view_paid_list', event_id=event.id)


def view_personal_paid_list(request, event_id):
    personal_event = PersonalEvent.objects.get(pk=event_id)
    contributions = personal_event.contributions.filter(status='Paid').order_by('-created_at')
    return render(request, 'benevofy/view_personal_paid_list.html', {'event': personal_event, 'contributions': contributions})


def add_manual_personal_event_payment(request, event_id):
    if request.method == 'POST':
        form = PersonalContributionForm(request.POST)
