from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>Home page</h1>')