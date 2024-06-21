from django.shortcuts import render, redirect
from .forms import SettingForm

def settings(request):
    form = SettingForm(instance=request.user.member.logged_in_association)
    if request.method == 'POST':
        form = SettingForm(request.POST, request.FILES, instance=request.user.member.logged_in_association)
        if form.is_valid():
            form.save()
            return render(request, 'benevofy/association_settings.html', {'form': form, 'message': 'Settings saved successfully'})
    return render(request, 'benevofy/association_settings.html', {'form': form})
