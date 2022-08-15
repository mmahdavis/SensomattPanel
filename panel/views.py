"""Docstring."""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models.models import Bed, Nurse, Bed_History, Person
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import insertbed_form, insertbedhistory_form
from .forms import insertnurse_form, insertpatient_form
# from django.contrib.auth.models import User


''' ############################# START TEMP ################################'''


# @login_required
@csrf_protect
def index(request):
    """Docstring."""
    try:
        return render(request, 'temp/index.html', {})
    except Exception as e:
        return HttpResponse(e.args)


''' ############################# Nurse ################################'''


# @login_required
@csrf_protect
def all_nurses(request):
    """Docstring."""
    nurse = []
    try:
        if request.method == "POST":
            data = request.POST.get('data')
            for i in Nurse.objects.filter(Q(name__contains=data) | Q(username__contains=data) | Q(mobile__contains=data)):
                nurse.extend([(i.id, i.name, i.mobile, i.username, i.shift)])
            return render(request, 'temp/all_nurses.html', {'nurse': nurse, 'value': 'nurses', 'search': 'true'})
        else:
            for i in Nurse.objects.all():
                nurse.extend([(i.id, i.name, i.mobile, i.username, i.shift)])
            return render(request, 'temp/all_nurses.html', {'nurse': nurse, 'value': 'nurses'})
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def add_nurse(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def edit_nurse(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def nurse_profile(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


''' ############################# PATIENT ################################'''


# @login_required
@csrf_protect
def all_patients(request):
    """Docstring."""
    patients = []
    try:
        if request.method == "POST":
            data = request.POST.get('data')
            for i in Person.objects.filter(Q(name__contains=data) | Q(mobile__contains=data) | Q(age__contains=data)):
                patients.extend([(i.id, i.name, i.mobile, i.age, i.gender, i.sickness, i.bed)])
            return render(request, 'temp/all_patients.html', {'patients': patients, 'value': 'patients', 'search': 'true'})
        else:
            for i in Person.objects.all():
                patients.extend([(i.id, i.name, i.mobile, i.age, i.gender, i.sickness, i.bed)])
            return render(request, 'temp/all_patients.html', {'patients': patients, 'value': 'patients'})
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def add_patient(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def edit_patient(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def patient_profile(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


''' ############################# BED ################################'''


# @login_required
@csrf_protect
def bed_allotment(request):
    """Docstring."""
    beds = []
    try:
        if request.method == "POST":
            data = request.POST.get('data')
            for i in Bed.objects.filter(Q(number__contains=data) | Q(nurse__name__contains=data) | Q(person__name__contains=data)):
                beds.extend([(i.id, i.number, i.nurse, i.bedsore)])
            return render(request, 'temp/bed_allotment.html', {'beds': beds, 'value': 'beds', 'search': 'true'})
        else:
            for i in Bed.objects.all():
                try:
                    per = Person.objects.get(bed=i.id)
                    beds.extend([(i.id, i.number, i.nurse, per, i.bedsore)])
                except:
                    beds.extend([(i.id, i.number, i.nurse, None, i.bedsore)])
            return render(request, 'temp/bed_allotment.html', {'beds': beds, 'value': 'beds'})
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def add_bed_allotment(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def edit_bed_allotment(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


# @login_required
@csrf_protect
def nurse_bed_allotment(request):
    """Docstring."""
    try:
        pass
    except Exception as e:
        return HttpResponse(e.args)


''' ############################# END TEMP ################################'''
''' ########################## panel&User ################################'''


# @login_required
@csrf_protect
def panel(request):
    """Docstring."""
    try:
        return render(request, 'panel.html', {})
    except Exception as e:
        return HttpResponse(e.args)


''' ############################# SELECT ################################'''


# @login_required
@csrf_exempt
def select(request, value, id=1):
    """Docstring."""
    if value == 'beds':
        bed = []
        try:
            if request.method == "POST":
                data = request.POST.get('data')
                for i in Bed.objects.filter(Q(number__contains=data) | Q(nurse__name__contains=data) | Q(person__name__contains=data)):
                    bed.extend([(i.id, i.number, i.nurse, i.bedsore)])
                return render(request, 'show.html', {'bed': bed, 'value': 'beds', 'search': 'true'})
            else:
                for i in Bed.objects.all():
                    try:
                        per = Person.objects.get(bed=i.id)
                        bed.extend([(i.id, i.number, i.nurse, per, i.bedsore)])
                    except:
                        bed.extend([(i.id, i.number, i.nurse, None, i.bedsore)])
                return render(request, 'show.html', {'bed': bed, 'value': 'beds'})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'bed_history':
        bedhistory = []
        try:
            for i in Bed_History.objects.filter(bed=id):
                bedhistory.extend([(i.id, i.bed, i.date, i.person, i.sickness, i.nurse)])
            return render(request, 'show.html', {'bedhistory': bedhistory, 'value': 'bed_history'})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'nurses':
        nurse = []
        try:
            if request.method == "POST":
                data = request.POST.get('data')
                for i in Nurse.objects.filter(Q(name__contains=data) | Q(username__contains=data) | Q(mobile__contains=data)):
                    nurse.extend([(i.id, i.name, i.mobile, i.username, i.shift)])
                return render(request, 'show.html', {'nurse': nurse, 'value': 'nurses', 'search': 'true'})
            else:
                for i in Nurse.objects.all():
                    nurse.extend([(i.id, i.name, i.mobile, i.username, i.shift)])
                return render(request, 'show.html', {'nurse': nurse, 'value': 'nurses'})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'patients':
        patients = []
        try:
            if request.method == "POST":
                data = request.POST.get('data')
                for i in Person.objects.filter(Q(name__contains=data) | Q(mobile__contains=data) | Q(age__contains=data)):
                    patients.extend([(i.id, i.name, i.mobile, i.age, i.gender, i.sickness, i.bed)])
                return render(request, 'show.html', {'patients': patients, 'value': 'patients', 'search': 'true'})
            else:
                for i in Person.objects.all():
                    patients.extend([(i.id, i.name, i.mobile, i.age, i.gender, i.sickness, i.bed)])
                return render(request, 'show.html', {'patients': patients, 'value': 'patients'})
        except Exception as e:
            return HttpResponse(e.args)
    # elif value == 'nurseuser':
    #     nurse = []
    #     try:
    #         if request.method == "POST":
    #             data = request.POST.get('data')
    #             for i in User.objects.filter(Q(name__contains=data) | Q(username__contains=data) | Q(mobile__contains=data)):
    #                 nurse.extend([(i.id, i.fullname, i.email, i.username)])
    #             return render(request, 'show.html', {'nurse': nurse, 'value': 'nurses', 'search': 'true'})
    #         else:
    #             for i in User.objects.filter(groups__name='nurses'):
    #                 nurse.extend([(i.id, i.first_name, i.last_name, i.email, i.username)])
    #             return render(request, 'show.html', {'nurse': nurse, 'value': 'nurses'})
    #     except Exception as e:
    #         return HttpResponse(e.args)


''' ############################# INSERT ################################'''


# @login_required
@csrf_protect
def insert(request, value):
    """Docstring."""
    if value == 'beds':
        try:
            if request.method == "POST":
                form = insertbed_form(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('/panel/beds/show/')
                else:
                    return render(request, 'insert.html', {'form': form})
            else:
                form = insertbed_form()
                return render(request, 'insert.html', {'form': form})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'bed_history':
        try:
            if request.method == "POST":
                form = insertbedhistory_form()
                if form.is_valid():
                    form.save()
                    return redirect('/panel/beds/show/history/' + id)
                else:
                    return render(request, 'insert.html', {'form': form})
            else:
                form = insertbedhistory_form()
                return render(request, 'insert.html', {'form': form})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'nurses':
        try:
            if request.method == "POST":
                form = insertnurse_form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/panel/nurses/show/')
                else:
                    return render(request, 'insert.html', {'form': form})
            else:
                form = insertnurse_form()
                return render(request, 'insert.html', {'form': form})
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'patients':
        try:
            if request.method == "POST":
                form = insertpatient_form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/panel/patients/show/')
                else:
                    return render(request, 'insert.html', {'form': form})
            else:
                form = insertpatient_form()
                return render(request, 'insert.html', {'form': form})
        except Exception as e:
            return HttpResponse(e.args)


''' ############################# UPDATE ################################'''


# LoginRequiredMixin, 
class BedUpdate(UpdateView):
    """Docstring."""

    model = Bed
    fields = '__all__'
    template_name = 'update.html'


class BedHistoryUpdate(UpdateView):
    """Docstring."""

    model = Bed_History
    fields = '__all__'
    template_name = 'update.html'


class NurseUpdate(UpdateView):
    """Docstring."""

    model = Nurse
    fields = '__all__'
    template_name = 'update.html'


class PatientUpdate(UpdateView):
    """Docstring."""

    model = Person
    fields = '__all__'
    template_name = 'update.html'


''' ############################# DELETE ################################'''


# @login_required
@csrf_protect
def delete(request, value, id=0):
    """Docstring."""
    if value == 'beds':
        try:
            Bed.objects.get(id=id).delete()
            return redirect('/panel/beds/show/')
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'bed_history':
        try:
            Bed_History.objects.get(id=id).delete()
            return redirect('/panel/beds/show/')
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'nurses':
        try:
            Nurse.objects.get(id=id).delete()
            return redirect('/panel/nurses/show/')
        except Exception as e:
            return HttpResponse(e.args)
    elif value == 'patients':
        try:
            Person.objects.get(id=id).delete()
            return redirect('/panel/patients/show/')
        except Exception as e:
            return HttpResponse(e.args)
