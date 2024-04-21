from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Subject(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Grade(models.Model):
    value = models.IntegerField()
    date = models.DateField(default=datetime.now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

