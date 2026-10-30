from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def doctor(request):
    return render(request, 'main/doctor.html')

def services(request):
    return render(request, 'main/services.html') 

def contact(request):
    return render(request, 'main/contact.html') 

