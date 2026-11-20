from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import School, Classroom, Teacher, Student

class SchoolManagementAPITests(APITestCase):

    def setUp(self):
        self.school1 = School.objects.create(
            name="โรงเรียนวิทยาการ",
            abbreviation="ว.ก.",
            address="123 เชียงใหม่"
        )
        self.school2 = School.objects.create(
            name="โรงเรียนเทคโนโลยี",
            abbreviation="ท.ล.",
            address="456 กรุงเทพฯ"
        )

        self.classroom1 = Classroom.objects.create(
            school=self.school1,
            grade="ม.1",
            room="1"
        )
        self.classroom2 = Classroom.objects.create(
            school=self.school1,
            grade="ม.1",
            room="2"
        )

        self.teacher1 = Teacher.objects.create(
            firstname="สมชาย",
            lastname="ใจดี",
            gender="M"
        )
        self.teacher1.classrooms.add(self.classroom1, self.classroom2)

        self.student1 = Student.objects.create(
            classroom=self.classroom1,
            firstname="สมหญิง",
            lastname="เรียนเก่ง",
            gender="F"
        )

    # --- School API ---
    def test_create_and_filter_school(self):
        url = reverse('school-list')
        # Create
        data = {"name": "โรงเรียนสาธิต", "abbreviation": "ส.ธ.", "address": "789 เชียงใหม่"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 3)

        # Filter by name
        filter_res = self.client.get(url, {'name': 'วิทยาการ'})
        self.assertEqual(filter_res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(filter_res.data), 1)
        self.assertEqual(filter_res.data[0]['abbreviation'], "ว.ก.")

    def test_school_detail_counts(self):
        url = reverse('school-detail', args=[self.school1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['classroom_count'], 2)
        self.assertEqual(response.data['teacher_count'], 1)
        self.assertEqual(response.data['student_count'], 1)

    # --- Classroom API ---
    def test_classroom_detail_lists(self):
        url = reverse('classroom-detail', args=[self.classroom1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['teachers']), 1)
        self.assertEqual(response.data['teachers'][0]['firstname'], "สมชาย")
        self.assertEqual(len(response.data['students']), 1)
        self.assertEqual(response.data['students'][0]['firstname'], "สมหญิง")

    # --- Teacher API ---
    def test_filter_and_detail_teacher(self):
        list_url = reverse('teacher-list')
        # Filter school and gender
        response = self.client.get(list_url, {'school': self.school1.id, 'gender': 'M'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        detail_url = reverse('teacher-detail', args=[self.teacher1.id])
        detail_res = self.client.get(detail_url)
        self.assertEqual(len(detail_res.data['classrooms']), 2)

    # --- Student API
    def test_update_and_delete_student(self):
        detail_url = reverse('student-detail', args=[self.student1.id])
        patch_res = self.client.patch(detail_url, {'classroom': self.classroom2.id}, format='json')
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.classroom, self.classroom2)

        del_res = self.client.delete(detail_url)
        self.assertEqual(del_res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)