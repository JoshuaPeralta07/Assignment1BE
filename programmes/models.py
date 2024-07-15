from django.db import models


# Create your models here.
class StudentAttendance(models.Model):
    attendance = models.CharField(max_length=100)
    student_key = models.ForeignKey('Student', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attendance


class StudentMark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Programme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=15)
    duration = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + "-" + self.lecturer.name
