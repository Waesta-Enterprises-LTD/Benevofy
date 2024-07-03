from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from Auth.models import PasswordResetToken
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from Members.models import Member
from Associations.models import Association
from Payments.models import RegistrationPayment
from uuid import uuid4
from django.db.models import Q
import requests
from django.contrib import messages


def login_member(request):
    if request.user.is_authenticated:
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        return redirect('member-dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.member.email_verified:
                login(request, user)
                if user.is_authenticated:
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect('member-dashboard')
            else:
                verification_code = uuid4()
                user.member.verification_code = verification_code
                user.member.save()
                subject = 'Benevofy Email Verification'
                message = render_to_string('benevofy/verification_email.html', {
                    'user': user,
                    'verification_code': str(verification_code),
                    'request': request
                })
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [user.email]
                send_mail(subject, message.strip(), from_email, to_email, fail_silently=False, html_message=message)
                return render(request, 'benevofy/login_member.html', {'error': 'A verification email has been sent to your email.', 'username': username, 'password': password})
        else:
            return render(request, 'benevofy/login_member.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'benevofy/login_member.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if authenticate(request, username=username, password=password):
            login(request, authenticate(request, username=username, password=password))
            return redirect('benevofy:admin-dashboard')
        else:
            return render(request, 'benevofy/login_admin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'benevofy/login_admin.html')


def reset_password(request):
    if request.method == 'POST':
        reset_code = request.POST.get('reset_code')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user = PasswordResetToken.objects.get(token=reset_code).user
            user.user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login-member')
        else:
            return render(request, 'benevofy/reset_password.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'benevofy/reset_password.html')


def send_reset_code(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            try:
                user.member
            except Member.DoesNotExist:
                user.member = Member.objects.create(user=user)
                user.member.save()
            token = PasswordResetToken(user=user.member)
            token.save()

            # Create message
            context = {'token': token.token}
            html_message = render_to_string('benevofy/reset_template.html', context)

            # Send email
            send_mail(
                'Password Reset Code',
                '',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
                html_message=html_message
            )

            return redirect('reset-password')
        except User.DoesNotExist:
            return render(request, 'benevofy/send_reset_code.html', {'error': 'User does not exist'})
    else:
        return render(request, 'benevofy/send_reset_code.html')


def change_password(request):
    if request.method == 'POST':
        try:
            user = request.user.member.user
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if user.check_password(old_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    logout(request)
                    return redirect('login-member')
                else:
                    return render(request, 'benevofy/change_password.html', {'error': 'Passwords do not match'})
            else:
                return render(request, 'benevofy/change_password.html', {'error': 'Incorrect old password'})
        except User.DoesNotExist:
            return redirect('login-member')
    else:
        return render(request, 'benevofy/change_password.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        if password == confirm_password:
            try:
                User.objects.get(username=email)
                return render(request, 'benevofy/register.html', {'error': 'Email already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
                member = Member.objects.create(user=user, phone=phone, gender=gender)
                member.user = user
                member.save()
                messages.success(request, 'A verification link has been sent to your email.')
                return redirect('login-member')
        else:
            return render(request, 'benevofy/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'benevofy/register.html')

def switch_association(request, association_id):
    association = Association.objects.get(id=association_id)
    request.user.member.logged_in_association = association
    request.user.member.current_mode = 'Member'
    request.user.member.save()
    login(request, request.user)
    return redirect('member-dashboard')


def switch_to_personal_account(request):
    member = request.user.member
    member.logged_in_association = None
    member.current_mode = 'Personal'
    member.save()
    return redirect('member-dashboard')


def switch_to_member(request):
    request.user.member.current_mode = 'Member'
    request.user.member.save()
    return redirect('member-dashboard')

def switch_to_admin(request):
    request.user.member.current_mode = 'Admin'
    request.user.member.save()
    return redirect('member-dashboard')

def logout_user(request):
    logout(request)
    return redirect('login-member')


def verify_email(request, verification_code):
    try:
        member = Member.objects.get(verification_code=verification_code)
        member.email_verified = True
        member.save()
        messages.success(request, 'Account verified successfully')
        return redirect('login-member')
    except Member.DoesNotExist:
        return redirect('login-member')



def register_exists(request, registration_code):
    logout(request)
    association_id = request.POST.get('association')
    association = Association.objects.get(Q(registration_code=registration_code) | Q(registration_code_paid=registration_code))
    paid = (registration_code == association.registration_code_paid)
    if request.method == 'POST':
        email = request.POST.get('email')
        member = Member.objects.get(user__email=email)
        try:
            association.members.get(user__email=email)
            return render(request, 'benevofy/enter_email.html', {'error': 'User already registered in this association.', 'registration_code': str(association.registration_code), 'association': association, 'paid': (paid == 'true')})
        except ObjectDoesNotExist:
            pass
        if paid == 'true':
            paid = True
            association.members.add(member)
            member.associations.add(association)
            member.logged_in_association = association
            member.save()
            association.registration_code_paid = uuid4()
            association.save()
            member.current_mode = 'Member'
            member.save()
            reference = str(uuid4())
            registration = RegistrationPayment.objects.create(user=member.user, association=association, reference=reference, status='Paid')
            return redirect('login-member')
        else:
            paid = False
            phone = request.POST.get('phone')
            reference = str(uuid4())
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
                return render(request, 'benevofy/enter_email.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'paid': paid, 'association': association, 'registration_code': str(association.registration_code)})
            payload = {
                "account_no": association.rel_account,
                "reference": reference,
                "msisdn": '+'+phone,
                "currency": currency,
                "amount": int(association.registration_fee),
                "description": "Registration Fee Payment Request."
            }
            response = requests.request("POST", url, headers=headers, json=payload)
            response = response.json()
            print(response)
            if response['success']:
                payment = RegistrationPayment.objects.create(
                    user=member,
                    association=association,
                    reference=reference,
                    amount_paid=association.registration_fee,
                )
                return redirect('login-member')
            else:
                return render(request, 'benevofy/enter_email.html', {'member': member, 'error': 'Failed to make payment. Contact support.', 'paid': paid, 'association': association, 'registration_code': str(association.registration_code)})
    else:
        return render(request, 'benevofy/enter_email.html', {'association': association, 'registration_code': str(association.registration_code), 'paid': paid})


