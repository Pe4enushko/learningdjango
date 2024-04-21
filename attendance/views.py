from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db import models

from attendance.forms import AttendanceForm
from grades.models import Attendance, Student, Subject

def index(request):
    context = {
        'attendance': Attendance.objects.all(),
        'form': AttendanceForm
    }
    return render(request, 'attendance/index.html' ,context)

def create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        form.save()
        return redirect('/attendance/')
    elif request.method == 'GET':
        form = AttendanceForm
        return render(request, 'attendance/edit.html', {'form': form})

def update(request, pk):
    att = Attendance.objects.get(id=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=att)
        if form.is_valid:
            form.save()
        return redirect('/attendance/')
    elif request.method == 'GET':
        return render(request, 'attendance/edit.html', {'form': AttendanceForm(instance=att)})


def delete(request, pk):
    obj = Attendance.objects.get(id=pk)
    obj.delete()
    return redirect('/attendance/')
