from django.urls import path
from .views import EventsCreateView

app_name= 'events'

urlpatterns = [
    path('', EventsCreateView.as_view(), name='appointment'),
]