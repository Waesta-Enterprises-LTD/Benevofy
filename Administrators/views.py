from django.shortcuts import render

def view_administrators(request):
    return render(request, 'benevofy/view_administrators.html')
