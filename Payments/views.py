from django.shortcuts import render
from django.http import HttpResponse
import json
from Contributions.models import EventContribution
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Events.models import Event
from Savings.models import Saving


def payment_initiated(request):
    return render(request, 'benevofy/payment_initiated.html')


@csrf_exempt
@require_http_methods(['POST'])
def webhook_receiver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contributions = EventContribution.objects.filter(reference=data['customer_reference'])
        if contributions.count() == 0:
            savings = Saving.objects.filter(reference=data['customer_reference'])
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
    contributions = EventContribution.objects.filter(event=event, status='Paid')
    return render(request, 'benevofy/view_paid_list.html', {'contributions': contributions, 'event': event})

