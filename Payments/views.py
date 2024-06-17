from django.shortcuts import render
from django.http import HttpResponse
import json
from Contributions.models import EventContribution
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def payment_initiated(request):
    return render(request, 'benevofy/payment_initiated.html')


@csrf_exempt
@require_http_methods(['POST'])
def webhook_receiver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contributions = EventContribution.objects.filter(reference=data['customer_reference'])
        if data['status'] == 'success':
            contributions.update(status='Paid')
        else:
            contributions.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
                

