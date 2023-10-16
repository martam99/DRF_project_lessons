from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Subscriber
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='mariam1@mail.ru'
        )
        self.user.set_password('mar000...')
        self.user.save()
        self.lesson = Lesson.objects.create(
            title='test',
            description='Test'
        )

    def test_list_lesson(self):
        """test for list of lessons"""
        response = self.client.get(
            reverse('lesson:lesson-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "title": "test",
                        "description": "Test",
                        "photo": "http://127.0.0.1:8000/media/no%20lesson%20photo",
                        "video_link": None,
                        "course": None,
                        "owner": None
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """test for creation lessons"""
        data = {
            'title': 'test2',
            'description': 'Test2'
        }
        response = self.client.post(
            reverse('lesson:lesson-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru'
        )
        self.user.set_password('test000+++')
        self.user.save()
        self.course = Course.objects.create(
            title='Russian language',
            description='grammar'
        )
        self.course.save()

    def test_create_sub(self):
        """test for creation subscribers"""
        data = {
            'user': self.user,
            'course': self.course
        }
        response = self.client.post(
            reverse('course:subscribers-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Subscriber.objects.all().count(),
            1
        )
