# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Event
from .forms import EventsModelForm
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

class EventsCreateView(CreateView):
    template_name = '../templates/appointment.html'
    form_class = EventsModelForm
    model = Event




