import datetime
from django import forms
from grades import models

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = '__all__'
        labels = {
            'student': 'студент',
            'date': 'дата',
            'subject': 'предмет'
        }
        widgets = {
            'date': forms.widgets.DateInput()
        }