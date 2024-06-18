from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from Auth.models import PasswordResetToken
from django.contrib.auth.models import User
from Members.models import Member
from Associations.models import Association
from uuid import uuid4

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


def register_member(request, registration_code):
    logout(request)
    try:
        association = Association.objects.get(registration_code=registration_code)
    except Association.DoesNotExist:
        return render(request, 'benevofy/register_member.html', {'error': 'Registration link expired. Please contact the association administrator.', 'expired': True})
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                return render(request, 'benevofy/register_member.html', {'error': 'Username already exists', 'first_name': first_name, 'last_name': last_name, 'registration_code': str(registration_code), 'association': association})
            elif User.objects.filter(email=email).exists():
                return render(request, 'benevofy/register_member.html', {'error': 'Email already exists', 'first_name': first_name, 'last_name': last_name, 'registration_code': str(registration_code), 'association': association})
            else:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                verification_code = uuid4()
                member = Member.objects.create(user=user, gender=gender)
                member.associations.add(association)
                member.logged_in_association = association
                member.phone = phone
                member.verification_code = verification_code
                member.save()
                association.registration_code = uuid4()
                association.save()
                subject = 'Benevofy Email Verification'
                message = render_to_string('benevofy/verification_email.html', {
                    'user': user,
                    'verification_code': str(verification_code),
                    'request': request
                })
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [user.email]
                send_mail(subject, message, from_email, to_email, fail_silently=False, html_message=message)
                return redirect('login-member')
        else:
            return render(request, 'benevofy/register_member.html', {'error': 'Passwords do not match', 'first_name': first_name, 'last_name': last_name, 'registration_code': str(registration_code), 'association': association})
    else:
        return render(request, 'benevofy/register_member.html', {'registration_code': str(registration_code), 'association': association, 'expired': False})

def logout_user(request):
    logout(request)
    return redirect('login-member')


def verify_email(request, verification_code):
    try:
        member = Member.objects.get(verification_code=verification_code)
        member.email_verified = True
        member.save()
        return redirect('login-member')
    except Member.DoesNotExist:
        return redirect('login-member')