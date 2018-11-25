from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile
from bookkeeping.models import Account
from bookkeeping.models import ExecutiveBook

# Create your views here.
def home_view(request, *args, **kwargs):
    print (request.user)
    return render(request, "home.html", {}) # string of html code not html

def contact_view(request, *args, **kwargs):
    print (request.user)
    return render(request, "contact.html", {})

def profile_view(request, *args, **kwargs):
    User = Profile.objects.get(user=request.user)
    Paper = ExecutiveBook.objects.filter(user=request.user)
    User = Profile.objects.get(user=request.user)
    name = ExecutiveBook.objects.get(user=request.user)
    accounts = Account.objects.filter(profile=name)[:5]
    context = {
        'user': User,
        'book': Paper,
        'my_list': accounts
    }
    return render(request, "profile.html", context)