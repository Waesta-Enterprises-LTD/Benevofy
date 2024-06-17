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



@login_required(login_url='login-member')
def member_dashboard(request):
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
    return render(request, 'benevofy/member_dashboard.html', {'events': events, 'members': members, 'polls': polls, 'member_count': member_count, 'html_content': html_content})


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
    return render(request, 'benevofy/members.html', {'members': members})

