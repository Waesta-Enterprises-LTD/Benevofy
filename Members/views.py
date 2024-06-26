from django.shortcuts import render
from .models import Member
from Events.models import Event
from Polls.models import Poll
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
import plotly.graph_objects as go
import plotly.io as pio
from Suspensions.forms import SuspensionForm
from PIL import Image, ImageFont, ImageDraw
from django.http import HttpResponse, FileResponse
import os
from io import BytesIO
from datetime import datetime, timedelta
from barcode import EAN13 
from barcode.writer import ImageWriter 
import random
from django.db import models



@login_required(login_url='login-member')
def member_dashboard(request):
    if request.user.member.logged_in_association:
        events = Event.objects.filter(status='Active', association=request.user.member.logged_in_association)
        paginator = Paginator(Member.objects.filter(associations=request.user.member.logged_in_association), 6)
        page = request.GET.get('page')
        members = paginator.get_page(page)
        member_count = Member.objects.filter(associations=request.user.member.logged_in_association).count()
        polls = Poll.objects.filter(association=request.user.member.logged_in_association)
        labels = ['PAID', 'UNPAID']
        values = [30, 40]

        # Create the donut chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, 
                                    marker=dict(colors=['green', 'red'], 
                                                line=dict(color='black', width=1)))])
        fig.update_layout(
            autosize=True,
            margin=dict(
                l=10,
                r=10,
                b=10,
                t=10,
                pad=4
            ),
            annotations=[dict(
                showarrow=False,
                text="",
                x=0.5,
                y=0.5
            )],
            width=300,
            height=300
        )
        
        # Convert the Plotly figure to JSON
        html_content = pio.to_html(fig, full_html=False)
        association = request.user.member.logged_in_association
        participated_events_last_10 = association.events.filter(contributions__user=request.user.member).order_by('-created_at')[:10].count()
        try:
            last_10 = (participated_events_last_10 / association.events.all().count()) * 100
        except ZeroDivisionError:
            last_10 = 0
        try:
            overall_participation = (association.events.filter(contributions__user=request.user.member).count() / association.events.all().count()) * 100
        except ZeroDivisionError:
            overall_participation = 0
        form = SuspensionForm()
        return render(request, 'benevofy/member_dashboard.html', {'events': events, 'members': members, 'polls': polls, 'member_count': member_count, 'html_content': html_content, 'last_10': last_10, 'overall_participation': overall_participation, 'form': form})
    else:
        events = request.user.member.events.filter(status='Active')
        total_contributions = events.annotate(contributions_count=models.Count('contributions')).aggregate(total=models.Sum('contributions_count'))['total']
        total_pledges = events.annotate(pledges_count=models.Count('pledges')).aggregate(total=models.Sum('pledges_count'))['total']
        return render(request, 'benevofy/member_dashboard.html', {'events': events, 'total_contributions': total_contributions, 'total_pledges': total_pledges})


def profile(request):
    return render(request, 'benevofy/profile.html')

def member_profile(request, member_id):
    return render(request, 'benevofy/member_profile.html', {'member': Member.objects.get(pk=member_id)})

def settings(request):
    if request.method == 'POST':
        picture = request.FILES.get('picture')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        request.user.member.picture = picture
        request.user.member.phone = phone
        request.user.member.gender = gender
        request.user.member.save()
    return render(request, 'benevofy/settings.html')


def view_members(request):
    query = request.GET.get('search')
    form = SuspensionForm()
    if query:
        members = Member.objects.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__email__icontains=query)
        ).filter(associations=request.user.member.logged_in_association)
    else:
        members = Member.objects.filter(associations=request.user.member.logged_in_association)
    paginator = Paginator(members, 6)
    page = request.GET.get('page')
    members = paginator.get_page(page)
    return render(request, 'benevofy/members.html', {'members': members, 'form': form})



def create_barcode(member):
    qnumber = str(random.randint(100000000000, 999999999999))+'0'+str(member.pk)
    my_code = EAN13(qnumber, writer=ImageWriter())
    img = my_code.save('barcode')
    img = open('barcode.png', 'rb')
    return img



def generate_id_card(request):
    image = Image.open('id_card_male-01.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 30)
    member = Member.objects.get(pk=request.user.member.pk)
    draw.text((485, 225), f"{member.user.first_name} {member.user.last_name}", font=font, fill=(0, 0, 0))
    draw.text((485, 295), f"{member.user.email}", font=font, fill=(0, 0, 0))
    draw.text((485, 365), f"{member.phone}", font=font, fill=(0, 0, 0))
    draw.text((640, 435), f"{member.biodata.date_of_birth.strftime('%d/%m/%Y')}", font=font, fill=(0, 0, 0))
    generated_on = datetime.now().strftime("%d/%m/%Y")
    expiry_date = (datetime.now() + timedelta(days=365)).strftime("%d/%m/%Y")
    draw.text((500, 570), f"{generated_on}", font=font, fill=(0, 0, 0))
    draw.text((840, 570), f"{expiry_date}", font=font, fill=(0, 0, 0))
    bar_code = create_barcode(member)
    bar_code = Image.open(bar_code).resize((380, 110))
    image.paste(bar_code, (5, 500))
    card_path = f'{member.user.first_name}-id_card.jpg'
    card_io = BytesIO()
    image.save(card_io, format='JPEG')
    card_io.seek(0)
    return FileResponse(card_io, as_attachment=True, filename=card_path)



