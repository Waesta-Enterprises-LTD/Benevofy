from django.shortcuts import render, redirect
from .forms import ItemForm
from Events.models import Event, PersonalEvent
from .models import Budget, Item

def view_budgets(request):
    form = ItemForm()
    return render(request, 'benevofy/budgets.html', {'form': form})


def add_item_to_budget(request, event_id):
    event = PersonalEvent.objects.get(pk=event_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            if event.budget:
                event.budget.items.add(item)
            else:
                budget = Budget.objects.create(event=event)
                event.budget = budget
                event.save()
                budget.items.add(item)
            item.budget = event.budget
            item.save()
            return redirect('view_budget_items', event_id=event.id)


def edit_item_in_budget(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_budget_items', event_id=item.budget.event.id)


def view_budget_items(request, event_id):
    event = PersonalEvent.objects.get(pk=event_id)
    items = event.budget.items.all()
    form = ItemForm()
    return render(request, 'benevofy/view_budget_items.html', {'items': items, 'event': event, 'form': form, 'budget': event.budget})


def mark_item_as_cleared(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.cleared = True
    item.save()
    return redirect('view_budget_items', event_id=item.budget.event.id)


def delete_item_from_budget(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('view_budget_items', event_id=item.budget.event.id)