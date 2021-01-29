from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    # Instead of returning an http response, we return a rendering of the template. Pass the renter function the location and the request
    return render(request, 'pages/about.html')