from rest_framework import serializers
from programmes.models import Programme, Lecturer, Student, StudentAttendance, StudentMark


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ['id', 'name', 'description', 'lecturer', 'level', 'duration']


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'department', 'email', 'phone', 'address']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone', 'address']


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ['id', 'attendance', 'student_key']


class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = ['id', 'student', 'mark']