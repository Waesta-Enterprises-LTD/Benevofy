from django.shortcuts import render
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from Events.models import Event
from Contributions.models import EventContribution
import logging
from .forms import ContributeEventForm, ContributionForm
from uuid import uuid4
import requests
from django.http import HttpResponse
from django.shortcuts import redirect


logger = logging.getLogger(__name__)


def select_events(request):
    form = ContributeEventForm()
    form.fields['events'].queryset = Event.objects.filter(association=request.user.member.logged_in_association, status='Active')
    return render(request, 'benevofy/select_events.html', {'form': form})


def pay_for_events(request):
    if request.method == 'POST':
        event_ids = request.POST.getlist('events')
        events = Event.objects.filter(pk__in=event_ids)
        forms = []
        for event in events:
            form = ContributionForm(initial={'event': event})
            form.fields['event'].disabled = True
            forms.append(form)
        form = forms
        member = request.user.member
        return render(request, 'benevofy/pay.html', {'member': member, 'events': events, 'forms': forms})
    else:
        return redirect('select_events')


def request_to_pay(request):
    if request.method == 'POST':
        member = request.user.member
        phone = request.POST.get('phone')
        event_ids = request.POST.getlist('events')
        events = Event.objects.filter(pk__in=event_ids)
        total_amount = 0
        reference = str(uuid4())
        for event_id in event_ids:
            event = Event.objects.get(pk=event_id)
            print(request.POST)
            amount = request.POST.get(f'amount-{event_id}')
            total_amount += float(amount)
            contribution = EventContribution.objects.create(
                user=member,
                event=event,
                reference=reference,
                amount=amount
            )
        url = "https://payments.relworx.com/api/mobile-money/request-payment"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.relworx.v2",
            "Authorization": "Bearer ec719b1a0db84d.YNrIn4iWVanw1Y0ptYvrVA"
        }
        if phone.startswith('256'):
            currency = 'UGX'
        elif phone.startswith('254'):
            currency = 'KES'
        else:
            return render(request, 'benevofy/pay.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'events': events})
        payload = {
            "account_no": member.logged_in_association.rel_account,
            "reference": reference,
            "msisdn": '+'+phone,
            "currency": currency,
            "amount": total_amount,
            "description": "Events Payment Request."
        }
        response = requests.request("POST", url, headers=headers, json=payload)
        print(response.json())
        return redirect('payment_initiated')