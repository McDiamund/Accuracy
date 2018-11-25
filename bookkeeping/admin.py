from django.contrib import admin
from .models import ExecutiveBook
from .models import Record
from .models import Account

# Register your models here.
admin.site.register(ExecutiveBook)
admin.site.register(Record)
admin.site.register(Account)