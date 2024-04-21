import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import BadRequest
from . import forms
from .models import Grade, Student, Subject
# Create your views here.

def index(request):
    context = {
        'grades': Grade.objects.all(),
        'form': forms.GradeModelForm
    }
    return render(request, 'grades/index.html', context)

def create(request):
    if request.method == 'POST':
        post = request.POST

        form = forms.GradeModelForm(post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь добавлен')
        else:
            messages.warning(request, 'Форма заполнена неправильно')

        return redirect('/')
    else:
        context = {
            'form': forms.GradeModelForm
        }
        return render(request, 'grades/create.html', context)

def update(request, pk):
    grade = Grade.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.GradeModelForm(instance=grade)
        return render(request, 'grades/edit.html', {'form': form})
    elif request.method == 'POST':
        form = forms.GradeModelForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Оценка обновлена')
            return redirect('/')
        else:
            messages.warning(request, 'Ошибка. Оценка не обновлена')
            return redirect('/')


def delete(request, pk):
    Grade.objects.get(id=pk).delete()
    return redirect('/')