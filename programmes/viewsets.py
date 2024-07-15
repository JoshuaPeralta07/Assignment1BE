from rest_framework import viewsets

from programmes.models import Programme, Lecturer, Student, StudentAttendance, StudentMark
from programmes.serializers import ProgrammeSerializer, LecturerSerializer, StudentSerializer, StudentMarkSerializer, \
    StudentAttendanceSerializer


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer


class StudentAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
