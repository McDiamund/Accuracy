from django.urls import path
from .views import AccountListView, AccountDetailView, AccountCreateView, AccountUpdateView, AccountDeleteView, annualreport_view,RecordCreateView, RecordUpdateView, RecordDeleteView
from bookkeeping.views import bookkeeping_view

app_name= 'bookkeeping'

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('report/', annualreport_view, name='annual-report'),
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='account-create'),
    path('<int:pk>/rec-create/', RecordCreateView.as_view(), name='record-create'),
    path('<int:pk>-rec/rec-update/', RecordUpdateView.as_view(), name='record-create'),
    path('<int:pk>-rec/rec-delete/', RecordDeleteView.as_view(), name='record-delete')
]