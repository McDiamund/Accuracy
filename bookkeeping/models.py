from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.db.models import F, FloatField, Sum

# Create your models here.

class ExecutiveBook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = ExecutiveBook.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

class Account (models.Model):
    name = models.TextField(max_length=100, null=True)
    balance = models.DecimalField(max_digits= 20, decimal_places=2, null=True)
    profile = models.ForeignKey(ExecutiveBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/bookkeeping'

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(Account, self).save(*args, **kwargs)
        if is_new:
            rec =  Record(date=0, details='First Record', income=0, expenses=0, list=self)
            rec.save()


class Record(models.Model):
        date = models.TextField(max_length=8, null=True)
        details = models.TextField(max_length=250, null=True)
        income = models.DecimalField(max_digits=20, decimal_places=2, null=True, default=0)
        expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
        def _get_total(self):
            if self.income in ['0', None] or self.expenses in ['0', None]:
                return self.income
            return self.income - self.expenses

        balance = property(_get_total)

        list = models.ForeignKey(Account, null=True, blank=True,on_delete=models.CASCADE)

        def get_absolute_url(self):
            return "/bookkeeping"

