from django.shortcuts import render

def biodata(request):
    return render(request, 'benevofy/biodata.html')