from django.shortcuts import render
from .models import Pledge
from Events.models import PersonalEvent
from .forms import PledgeForm
from django.core.paginator import Paginator

def view_pledges(request, event_id):
    event = PersonalEvent.objects.get(id=event_id)
    return render(request, 'benevofy/view_pledges.html', {'event': event})


def pledge(request, event_id):
    event = PersonalEvent.objects.get(id=event_id)
    form = PledgeForm()
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.instance.event = event
            form.save()
            return render(request, 'benevofy/pledge.html', {'event_id': event_id})
    return render(request, 'benevofy/pledge.html', {'event': event, 'form': form})