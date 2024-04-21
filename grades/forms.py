import datetime

from django import forms
from learning import settings
from . import models


class GradeModelForm(forms.ModelForm):
    class Meta:
        model = models.Grade
        fields = ['value', 'date', 'student', 'subject']
        labels = {
            'value': 'оценка',
            'date': 'дата',
            'student': 'студент',
            'subject': 'предмет'
        }
        widgets = {
            'date': forms.widgets.DateInput()
        }

# class GradeForm(forms.Form):
#     value = forms.IntegerField()

#     date = forms.DateField(label='date',
#                            widget=forms.widgets.DateInput,
#                            initial=datetime.datetime.now().__format__('%d.%m.%Y')
#                            )

#     student = forms.ModelChoiceField(queryset=models.Student.objects.all())
#     subject = forms.ModelChoiceField(queryset=models.Subject.objects.all())

#     def save(self, post):
#         models.Grade(value=post['value'], 
#               date=datetime.datetime.strptime(post['date'], '%d.%m.%Y'),
#               student=models.Student.objects.get(pk=post['student']),
#               subject=models.Subject.objects.get(pk=post['subject'])).save()
