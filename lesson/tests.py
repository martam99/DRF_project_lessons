from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from course.models import Course, Subscriber
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='mariam1@mail.ru',
            is_active=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.user.set_password('mar000...')
        self.user.save()
        self.lesson = Lesson.objects.create(
            title='test',
            description='Test',
            owner=self.user,
            video_link='https://www.youtube.com/watch?v=1HtEPEn4-LY'
        )
        self.course = Course.objects.create(
            title='course1',
            description='Course1',
            owner=self.user
        )
        self.course.save()

    def test_create_lesson(self):
        """test for creation lessons"""
        data = {
            'title': self.lesson.title,
            'description': self.lesson.description,
            'course': self.course.id,
            'video_link': self.lesson.video_link
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
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        "id": 1,
                        "title": "test",
                        "description": "Test",
                        "photo": None,
                        "video_link": self.lesson.video_link,
                        "course": None,
                        "owner": 1
                    }
                ]
            }
        )

    def tearDown(self):
        User.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()


class SubTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.ru',
            is_active=True
        )
        self.user.set_password('test000+++')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Russian language',
            description='grammar',
            owner=self.user
        )
        self.sub = Subscriber.objects.create(
            course=self.course,
        )

    def test_create_sub(self):
        """test for creation subscribers"""
        data = {
            'course': self.course.id,
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
            2
        )

    def tearDown(self):
        User.objects.all().delete()
        Lesson.objects.all().delete()
        Subscriber.objects.all().delete()
