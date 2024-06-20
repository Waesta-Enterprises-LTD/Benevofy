from django.shortcuts import render, redirect
from .forms import LoanRequestForm
from .models import LoanRequest
from Loans.models import Loan
from uuid import uuid4
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def request_loan(request):
    member = request.user.member
    form = LoanRequestForm()
    form.fields['guarantors'].queryset = member.logged_in_association.members.all()
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            receiver_number = form.cleaned_data['recieving_number']
            receiver_number = str(receiver_number)
            if receiver_number.startswith('256') or receiver_number.startswith('254'):
                form.instance.member = member
                form.instance.association = member.logged_in_association
                form.instance.reference = str(uuid4())
                form.instance.user = member
                form.save()
                guarantors = form.cleaned_data['guarantors']
                for guarantor in guarantors:
                    subject = 'Request to guarant Loan'
                    message = render_to_string('benevofy/request_to_guarant.html', {'request': form.instance, 'guarantor': guarantor})
                    from_email = settings.DEFAULT_FROM_EMAIL
                    recipient_list = [member.user.email]
                    send_mail(subject, message, from_email, recipient_list)
                return redirect('view_loan_requests')
            else:
                return render(request, 'benevofy/request_loan.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'form': form})
    return render(request, 'benevofy/request_loan.html', {'member': member, 'form': form})


def view_loan_requests(request):
    requests = LoanRequest.objects.filter(association=request.user.member.logged_in_association)
    return render(request, 'benevofy/view_loan_requests.html', {'requests': requests})


def approve_loan_request(request, request_id):
    loan_request = LoanRequest.objects.get(id=request_id)
    loan_request.status = 'Approved'
    loan_request.save()
    loan = Loan(
        user=request.user.member,
        association=loan_request.association,
        amount=loan_request.amount,
        interest_rate=request.user.member.logged_in_association.loan_interest_rate,
        repayment_date=loan_request.repayment_date,
    )
    loan.save()
    return redirect('view_loans')


def approve_as_guarantor(request, reference, member_id):
    member = Member.objects.get(id=member_id)
    loan_request = LoanRequest.objects.get(reference=reference)
    loan_request.approved_guarantors.add(member)
    return redirect('approved_as_guarantor')


def approved_as_guarantor(request):
    return render(request, 'benevofy/approved_as_guarantor.html')
