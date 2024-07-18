# tests.py
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Programme, Lecturer, Student
from .serializers import ProgrammeSerializer, LecturerSerializer, StudentSerializer, UserSerializer


class ProgrammeViewSetTestCase(APITestCase):
    def setUp(self):
        self.programme1 = Programme.objects.create(name="Programme 1", description="Description 1", level=6,
                                                   duration="1 year")
        self.programme2 = Programme.objects.create(name="Programme 2", description="Description 2", level=5,
                                                   duration="1 year")
        self.list_url = reverse('programme-list')
        self.detail_url = lambda pk: reverse('programme-detail', args=[pk])

    def test_get_programme_list(self):
        response = self.client.get(self.list_url)
        programmes = Programme.objects.all()
        serializer = ProgrammeSerializer(programmes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_programme_detail(self):
        response = self.client.get(self.detail_url(self.programme1.pk))
        programme = Programme.objects.get(pk=self.programme1.pk)
        serializer = ProgrammeSerializer(programme)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_programme(self):
        data = {'name': 'Programme 3', 'description': 'Description 3', 'level': 6, 'duration': '1 year'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Programme.objects.count(), 3)
        self.assertEqual(Programme.objects.get(pk=response.data['id']).name, 'Programme 3')

    def test_update_programme(self):
        data = {'name': 'Updated Programme 1', 'description': 'Updated Description 1', 'level': 5, 'duration': '1 year'}
        response = self.client.put(self.detail_url(self.programme1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.programme1.refresh_from_db()
        self.assertEqual(self.programme1.name, 'Updated Programme 1')
        self.assertEqual(self.programme1.description, 'Updated Description 1')

    def test_delete_programme(self):
        response = self.client.delete(self.detail_url(self.programme1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Programme.objects.count(), 1)


class LecturerViewSetTest(APITestCase):

    def setUp(self):
        self.lecturer1 = Lecturer.objects.create(name='John Doe', department='Math', email='j9OqFP@example.com',
                                                 phone='1234567890', address='123 Main Street')
        self.lecturer2 = Lecturer.objects.create(name='Jane Doe', department='Science', email='jnYqFP@example.com',
                                                 phone='9876543210', address='456 Oak Street')
        self.valid_payload = {
            'name': 'Albert Einstein',
            'department': 'Physics',
            'email': '9OqFP@example.com',
            'phone': '1234567890',
            'address': '123 Main Street'
        }
        self.invalid_payload = {
            'name': '',
            'department': 'Chemistry',
            'email': 'nYqFP@example.com',
            'phone': '9876543210',
            'address': '456 Oak Street'
        }

    def test_get_all_lecturers(self):
        response = self.client.get(reverse('lecturer-list'))
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        # print(response.data)  # Debugging statement
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_lecturer(self):
        response = self.client.post(reverse('lecturer-list'), data=self.valid_payload)
        # print(response.data)  # Debugging statement
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lecturer.objects.count(), 3)
        self.assertEqual(Lecturer.objects.get(id=response.data['id']).name, 'Albert Einstein')

    def test_create_invalid_lecturer(self):
        response = self.client.post(reverse('lecturer-list'), data=self.invalid_payload)
        # print(response.data)  # Debugging statement
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_lecturer(self):
        response = self.client.get(reverse('lecturer-detail', kwargs={'pk': self.lecturer1.pk}))
        serializer = LecturerSerializer(self.lecturer1)
        # print(response.data)  # Debugging statement
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lecturer(self):
        updated_payload = {
            'name': 'John Updated',
            'department': 'Math Updated',
            'email': 'j9OqFP@example.com',
            'phone': '1234567890',
            'address': '123 Main Street'
        }
        response = self.client.put(reverse('lecturer-detail', kwargs={'pk': self.lecturer1.pk}), data=updated_payload)
        # print(response.data)  # Debugging statement
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lecturer.objects.get(pk=self.lecturer1.pk).name, 'John Updated')

    def test_delete_lecturer(self):
        response = self.client.delete(reverse('lecturer-detail', kwargs={'pk': self.lecturer1.pk}))
        # print(response.data)  # Debugging statement
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lecturer.objects.count(), 1)


class StudentViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {'name': 'John Doe', 'email': 'j9OqFP@example.com', 'phone': '1234567890', 'address': '123 Main Street', 'attendance': True, 'student_mark': 80}
        self.student = Student.objects.create(**self.student_data)
        self.valid_payload = {'name': 'Jane Doe', 'email': 'jnYqFP@example.com', 'phone': '9876543210', 'address': '456 Oak Street', 'attendance': False, 'student_mark': 90}
        self.invalid_payload = {'name': '', 'email': 'nYqFP@example.com', 'phone': '9876543210', 'address': '456 Oak Street', 'attendance': False, 'student_mark': 90}

    def test_get_all_students(self):
        response = self.client.get(reverse('student-list'))
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_student(self):
        response = self.client.post(
            reverse('student-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        response = self.client.post(
            reverse('student-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_student(self):
        response = self.client.get(
            reverse('student-detail', kwargs={'pk': self.student.pk})
        )
        student = Student.objects.get(pk=self.student.pk)
        serializer = StudentSerializer(student)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        response = self.client.put(
            reverse('student-detail', kwargs={'pk': self.student.pk}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(
            reverse('student-detail', kwargs={'pk': self.student.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com'
        }
        self.invalid_payload = {
            'username': '',
            'password': 'password123',
            'email': 'newuser@example.com'
        }

    def test_register_valid_user(self):
        response = self.client.post(
            reverse('register'),  # Make sure 'register' is the name of the URL pattern for the RegisterView
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')

    def test_register_invalid_user(self):
        response = self.client.post(
            reverse('register'),  # Make sure 'register' is the name of the URL pattern for the RegisterView
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)