"""Accuracy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from pages.views import contact_view
from pages.views import profile_view
from pages.views import appointment_view
from pages.views import our_staff_view
from pages.views import about_view
from django.conf.urls.static import static
from pages.views import internal_audit

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('staff/', our_staff_view, name='our_staff'),
    path('bookkeeping/', include('bookkeeping.urls')),
    path('appointment/', include('events.urls')),
    path('about/', about_view, name="about"),
    path('audit/', internal_audit, name="iaudit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)