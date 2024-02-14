from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>This is a website that allows a better library organization</h1>')