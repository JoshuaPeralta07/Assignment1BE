from django.contrib import admin

from programmes.models import Programme, Lecturer, Student, StudentAttendance, StudentMark

# Register your models here.
admin.site.register(Programme)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(StudentAttendance)
admin.site.register(StudentMark)