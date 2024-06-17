from django.shortcuts import render
from django.http import HttpResponse
import json
from Contributions.models import EventContribution
import logging

def payment_initiated(request):
    return render(request, 'benevofy/payment_initiated.html')



def webhook_receiver(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            contributions = EventContribution.objects.filter(reference=data['customer_reference'])
            if data['status'] == 'success':
                contributions.update(status='Paid')
            else:
                contributions.delete()
            return HttpResponse(status=200)
        except Exception as e:
            logger.error('Error in webhook_receiver: %s', str(e))
            return HttpResponse(status=500)
    else:
        logger.error('Webhook received with method other than POST')
        return HttpResponse(status=405)
                

