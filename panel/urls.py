"""sensomatt URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, re_path
from . import views
from .views import BedUpdate, BedHistoryUpdate, PatientUpdate, NurseUpdate

app_name = 'panel'
urlpatterns = [
    path(r'', views.panel),
    path(r'temp/', views.index),
    path(r'temp/index/', views.index),
    # NURCES
    path(r'temp/all_nurses/', views.all_nurses),
    path(r'temp/add_nurse/', views.add_nurse),
    path(r'temp/edit_nurse/', views.edit_nurse),
    path(r'temp/nurse_profile/', views.nurse_profile),
    # PATIENT
    path(r'temp/all_patients/', views.all_patients),
    path(r'temp/add_patient/', views.add_patient),
    path(r'temp/edit_patient/', views.edit_patient),
    path(r'temp/patient_profile/', views.patient_profile),
    # BEDS
    path(r'temp/bed_allotment/', views.bed_allotment),
    path(r'temp/add_bed_allotment/', views.add_bed_allotment),
    path(r'temp/edit_bed_allotment/', views.edit_bed_allotment),
    path(r'temp/nurse_bed_allotment/', views.nurse_bed_allotment),

    # BEDS
    path(r'beds/show/', views.select, {'value': 'beds'}),
    re_path(r'beds/show/history/(?P<id>\d+)', views.select, {'value': 'bed_history'}),
    path(r'beds/new/', views.insert, {'value': 'beds'}),
    re_path(r'beds/new/history/', views.insert, {'value': 'bed_history'}),
    re_path(r'beds/edit/(?P<pk>\d+)', BedUpdate.as_view(success_url="/panel/beds/show/")),
    re_path(r'beds/edit/history/(?P<pk>\d+)', BedHistoryUpdate.as_view(success_url="/panel/beds/show/")),
    re_path(r'beds/delete/(?P<id>\d+)', views.delete, {'value': 'beds'}),
    re_path(r'beds/history/delete/(?P<id>\d+)', views.delete, {'value': 'bed_history'}),
    # NURCES
    path(r'nurses/show/', views.select, {'value': 'nurses'}),
    path(r'nurses/new/', views.insert, {'value': 'nurses'}),
    re_path(r'nurses/edit/(?P<pk>\d+)', NurseUpdate.as_view(success_url="/panel/nurse/show/")),
    re_path(r'nurses/delete/(?P<id>\d+)', views.delete, {'value': 'nurses'}),
    # PATIENT
    path(r'patients/show/', views.select, {'value': 'patients'}),
    path(r'patients/new/', views.insert, {'value': 'patients'}),
    re_path(r'patients/edit/(?P<pk>\d+)', PatientUpdate.as_view(success_url="/panel/patients/show/")),
    re_path(r'patients/delete/(?P<id>\d+)', views.delete, {'value': 'patients'}),
]
