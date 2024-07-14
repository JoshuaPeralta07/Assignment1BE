from django.contrib import admin

from programmes.models import Programme, Lecturer, Student, ParentInfo, StudentTuitionFee, StudentMark

# Register your models here.
admin.site.register(Programme)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(ParentInfo)
admin.site.register(StudentTuitionFee)
admin.site.register(StudentMark)