from django.shortcuts import render, get_list_or_404
from .models import ExecutiveBook
from .models import Account
from django.urls import reverse_lazy
from .models import Record
from django import forms
from pages.models import Profile
from django.contrib.auth.models import User
from .forms import AccountModelForm, RecordModelForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

# Create your views here.

class AccountListView(ListView):

    def get(self, request, *args, **kwargs):
        User = Profile.objects.get(user=request.user)
        name = ExecutiveBook.objects.get(user=request.user)
        accounts = Account.objects.filter(profile=name)
        context = {'ac': accounts,
                   'my_list': accounts,
                   'user': User,}
        return render(request, '../templates/bookkeeping.html', context)

class AccountDetailView(DetailView):
    template_name = '../templates/account-detail.html'
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        User = Profile.objects.get(user=request.user)
        id_ = self.kwargs['pk']
        account = Account.objects.get(id=id_)
        re = Record.objects.filter(list=account)
        my_list = get_list_or_404(re)
        context = {
            'my_list': my_list,
            'user': User,
            'account': account,
                   }
        return render(request, '../templates/account-detail.html', context)


class AccountCreateView(CreateView):
    template_name = '../templates/account-create.html'
    model = Account
    fields = [
        'name',
        'balance',
        'profile',
    ]

    def get(self, request, *args, **kwargs):
        User = Profile.objects.get(user=request.user)
        form = AccountModelForm(user=request.user)
        name = ExecutiveBook.objects.get(user=request.user)
        accounts = Account.objects.filter(profile=name)
        context = {'ac': accounts,
                   'my_list': accounts,
                   'user': User,
                   'form': form,
                }
        return render(request, '../templates/account-create.html', context)

class AccountUpdateView(UpdateView):
    template_name = '../templates/account-create.html'
    model = Account
    fields = [
        'name',
        'balance',
    ]


class AccountDeleteView(DeleteView):
    model = Account
    template_name = '../templates/account_confirm_delete.html'
    success_url = '/bookkeeping'

class RecordCreateView(CreateView):
    template_name = '../templates/record-create.html'
    model = Record
    fields = [
        'date',
        'details',
        'income',
        'expenses',
        'list',
    ]

    def get(self, request, *args, **kwargs):
        User = Profile.objects.get(user=request.user)
        id_ = self.kwargs['pk']
        name = ExecutiveBook.objects.get(user=request.user)
        form = RecordModelForm(user=id_)
        accounts = Account.objects.filter(profile=name)
        context = {'ac': accounts,
                   'my_list': accounts,
                   'user': User,
                   'form': form,
                }
        return render(request, '../templates/record-create.html', context)

class RecordUpdateView(UpdateView):
    template_name = '../templates/record-create.html'
    model = Record
    fields = [
        'date',
        'details',
        'income',
        'expenses',
        'list',
    ]

class RecordDeleteView(DeleteView):
    model = Record
    template_name = '../templates/record_confirm_delete.html'
    success_url = '/bookkeeping'

def annualreport_view(request, *args, **kwargs):
    User = Profile.objects.get(user=request.user)
    name = ExecutiveBook.objects.get(user=request.user)
    ac = Account.objects.filter(profile=name)
    context = {
        'Name': name,
        'Account': ac,
        'my_list': ac,
        'user': User
    }
    return render(request, "annualreport.html", context)


def bookkeeping_view(request, *args, **kwargs):
        User = Profile.objects.get(user=request.user)
        name = ExecutiveBook.objects.get(user=request.user)
        ac = Account.objects.filter(profile=name)
        context = {
            'Name': name,
            'Account': ac,
            'my_list': ac,
            'user': User
        }
        return render(request, "bookkeeping.html", context)