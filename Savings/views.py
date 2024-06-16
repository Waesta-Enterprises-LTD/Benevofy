from django.shortcuts import render
from .models import Saving
from .forms import SavingTargetForm, SavingForm

def save_money(request):
    member = request.user.member
    form = SavingForm()
    if request.method == 'POST':
        amount = request.POST.get('amount')
        Saving.objects.create(
            user=member,
            amount=amount
        )
        return render(request, 'benevofy/save_money.html', {'member': member})
    return render(request, 'benevofy/save_money.html', {'member': member, 'form': form})


def create_saving_target(request):
    if request.method == 'POST':
        form = SavingTargetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'benevofy/save_money.html')
    else:
        form = SavingTargetForm()
    return render(request, 'benevofy/create_saving_target.html', {'form': form})

def view_savings(request):
    savings = Saving.objects.all()
    return render(request, 'benevofy/view_savings.html', {'savings': savings})

