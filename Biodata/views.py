from django.shortcuts import render, redirect
from .forms import BiodataForm, DependentForm
from Biodata.models import Biodata, Dependent
from django import forms

def biodata(request):
    return redirect('profile')



def add_biodata(request):
    if request.method == 'POST':
        if request.user.member.biodata:
            form = BiodataForm(request.POST, instance=request.user.member.biodata)
        else:
            form = BiodataForm(request.POST)
        if form.is_valid():
            form.instance.member = request.user.member
            biodata = form.save()
            if not request.user.member.biodata:
                request.user.member.biodata = biodata
                request.user.member.save()
            return redirect('biodata')
    else:
        if request.user.member.biodata:
            form = BiodataForm(instance=request.user.member.biodata)
        else:
            form = BiodataForm()
    return render(request, 'benevofy/add_biodata.html', {'form': form})


def view_dependents(request):
    return render(request, 'benevofy/view_dependents.html')

def add_dependent(request):
    if request.method == 'POST':
        form = DependentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.dependent_to = request.user.member
            if request.user.member.biodata:
                form.instance.biodata = request.user.member.biodata
            else:
                biodata = Biodata(member=request.user.member)
                biodata.save()
                request.user.member.biodata = biodata
                request.user.member.save()
                form.instance.biodata = biodata
            dependent = form.save()
            request.user.member.biodata.dependents.add(dependent)
            return redirect('view_dependents')
    else:
        form = DependentForm()
    form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'})
    return render(request, 'benevofy/add_dependent.html', {'form': form})


def member_dependents(request, member_id):
    member = request.user.member.logged_in_association.members.get(id=member_id)
    if member.biodata:
        dependents = member.biodata.dependents.all()
    else:
        dependents = []
    return render(request, 'benevofy/member_dependents.html', {'member': member, 'dependents': dependents})


def edit_dependent(request, dependent_id):
    dependent = Dependent.objects.get(id=dependent_id)
    if request.method == 'POST':
        form = DependentForm(request.POST, request.FILES, instance=dependent)
        if form.is_valid():
            form.save()
            return redirect('view_dependents')
    else:
        form = DependentForm(instance=dependent)
    form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'})
    return render(request, 'benevofy/edit_dependent.html', {'form': form})