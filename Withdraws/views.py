from django.shortcuts import render
from .forms import WithdrawForm
from uuid import uuid4

def view_withdraws(request):
    form = WithdrawForm()
    return render(request, 'benevofy/view_withdraws.html', {'form': form})


def make_withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.member
            form.instance.association = request.user.member.logged_in_association
            form.save()
            return render(request, 'benevofy/payment_initiated.html')
   