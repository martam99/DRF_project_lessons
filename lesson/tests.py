from rest_framework import status
from rest_framework.test import APITestCase


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        data = {
            'title': 'test',
            'description': 'Test'
        }
        response = self.client.post(
            'lesson/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
