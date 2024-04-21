from django.contrib import admin
from .models import Grade, Student, Attendance, Subject

# Register your models here.
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Subject)
