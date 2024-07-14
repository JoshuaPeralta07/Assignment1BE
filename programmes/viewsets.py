from rest_framework import viewsets

from programmes.models import Programme, Lecturer, Student, ParentInfo, StudentTuitionFee, StudentMark
from programmes.serializers import ProgrammeSerializer, LecturerSerializer, StudentSerializer, ParentInfoSerializer, \
    StudentTuitionFeeSerializer, StudentMarkSerializer


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ParentInfoViewSet(viewsets.ModelViewSet):
    queryset = ParentInfo.objects.all()
    serializer_class = ParentInfoSerializer

class StudentTuitionFeeViewSet(viewsets.ModelViewSet):
    queryset = StudentTuitionFee.objects.all()
    serializer_class = StudentTuitionFeeSerializer

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
