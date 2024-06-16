from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Event
from .forms import EventForm
from django.core.paginator import Paginator
import xlsxwriter
from django import forms
from django.http import HttpResponse
import os
import tempfile


def events(request):
    events = Event.objects.all()
    paginator = Paginator(events, 10)
    page = request.GET.get('page')
    events = paginator.get_page(page)
    context = {'events': events}
    return render(request, 'benevofy/events.html', context)



def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('events')


def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return render(request, 'benevofy/events.html')
    else:
        form = EventForm(instance=event)
    return render(request, 'benevofy/update_event.html', {'form': form})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.instance.association = request.user.member.logged_in_association
            event = form.save()
            event.association.events.add(event)
            return redirect('events')
    else:
        association = request.user.member.logged_in_association
        form = EventForm(initial={'association': association})
        form.fields['association'].widget = forms.HiddenInput()
    return render(request, 'benevofy/create_event.html', {'form': form})


def event_report(request, event_id):
    event = Event.objects.get(id=event_id)
    contributions = event.contributions.all()

    # Create a workbook and a worksheet
    workbook = xlsxwriter.Workbook(f'event_report_{event.name}.xlsx')
    worksheet = workbook.add_worksheet()

    # Define the header row
    header_format = workbook.add_format({'bold': True})
    worksheet.write_row(0, 0, ['Contributor', 'Amount', 'Date'], header_format)

    # Write the data to the worksheet
    row = 1  # Start from row 1
    for contribution in contributions:
        worksheet.write(row, 0, contribution.member.name)
        worksheet.write(row, 1, contribution.amount)
        worksheet.write(row, 2, contribution.date)
        row += 1

    # Save the workbook to a temporary file and delete it afterwards
    with tempfile.NamedTemporaryFile(delete=True, suffix='.xlsx') as temp_file:
        workbook.close()
        temp_file.write(open(f'event_report_{event.name}.xlsx', 'rb').read())

    # Return the workbook as a response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=event_report_{event.name}.xlsx'
    with open(f'event_report_{event.name}.xlsx', 'rb') as file:
        response.write(file.read())

    os.remove(f'event_report_{event.name}.xlsx')
    return response

