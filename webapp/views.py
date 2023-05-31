from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required(login_url='/login/')
def about_me(request):
    return render(request, "about_me.html")

def contact(request):
    return render(request, "webapp/contact.html")

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, "dashboard.html")