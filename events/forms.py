from django import forms
from .models import Event

class EventsModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'day',
            'start_time',
            'end_time',
            'notes',
        ]