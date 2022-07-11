from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile


def home(request):
    mobiles = Mobile.objects.all()
    return render(request, 'home.html', {'mobiles': mobiles})


def page(request):
    return HttpResponse("Welcome to the second page")