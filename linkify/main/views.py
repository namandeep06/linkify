from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def about(request):
    return render(request, 'contact-success.html')

def contact(request):
    return render(request, 'contact-us.html')
