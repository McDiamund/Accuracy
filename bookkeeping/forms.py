from django import forms
from .models import Account, ExecutiveBook, Record
from django.contrib.auth.models import User
from pages.models import Profile
from urllib import request

class AccountModelForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    balance = forms.IntegerField(label='Balance')
    profile = forms.ModelChoiceField( queryset=ExecutiveBook.objects.none())

    class Meta:
        model = Account
        fields = ['name','balance', 'profile']

    def __init__(self, user, *args, **kwargs):
        super(AccountModelForm, self).__init__(*args, **kwargs)
        self.fields['profile'].queryset = ExecutiveBook.objects.filter(user=user)

class RecordModelForm(forms.ModelForm):
    list = forms.ModelChoiceField(queryset=Account.objects.none())

    class Meta:
        model = Record
        fields = [
            'date',
            'details',
            'income',
            'expenses',
            'list',
        ]

    def __init__(self, user, *args, **kwargs):
        super(RecordModelForm, self).__init__(*args, **kwargs)
        self.fields['list'].queryset = Account.objects.filter(id=user)