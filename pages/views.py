from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile
from bookkeeping.models import Account
from bookkeeping.models import ExecutiveBook
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

# Create your views here.
def home_view(request, *args, **kwargs):
    print (request.user)
    return render(request, "home.html", {}) # string of html code not html

def contact_view(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
          name = request.POST.get('name', '')
          email = request.POST.get('email', '')
          content = request.POST.get('content', '')

          template = get_template('contact_template.txt')
        context = {
            'name':name,
            'email':email,
            'content':content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Accuracy" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': email}
        )
        email.send()
        return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


def internal_audit(request, *args, **kwargs):
    User = Profile.objects.get(user=request.user)
    name = ExecutiveBook.objects.get(user=request.user)
    accounts = Account.objects.filter(profile=name)[:5]
    context = {
        'user': User,
        'my_list': accounts
    }
    return render(request, "iaudit.html", context)

def about_view(request, *args, **kwargs):
    print (request.user)
    return render(request, "about.html", {})

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

def our_staff_view(request, *args, **kwargs):

    return render(request, "our_staff.html", {})

def appointment_view(request, *args, **kwargs):
    User = Profile.objects.get(user=request.user)
    name = ExecutiveBook.objects.get(user=request.user)
    accounts = Account.objects.filter(profile=name)[:5]
    context = {
        'user': User,
        'my_list': accounts
    }
    return render(request, "appointment.html", context)
