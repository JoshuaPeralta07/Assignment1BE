from rest_framework import serializers
from programmes.models import Programme, Lecturer, Student, ParentInfo, StudentTuitionFee, StudentMark

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
        fields = ['id', 'name', 'email', 'parents_info', 'tuition_fee', 'student_mark', 'phone', 'address']

class ParentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentInfo
        fields = ['id', 'name', 'email', 'phone', 'address']

class StudentTuitionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTuitionFee
        fields = ['id', 'tuition_fee']

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = ['id', 'marks']