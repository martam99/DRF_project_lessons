from django.core.management import BaseCommand

from course.models import Course
from lesson.models import Lesson
from payments.models import Payment


class Command(BaseCommand):
    course = Course.objects.last()
    lesson = Lesson.objects.last()

    def handle(self, *args, **kwargs):
        payment_list = [
            {'paid_course': self.course, 'paid_lesson': self.lesson, 'payment_sum': 150000, 'payment_method': 'CASH'},
            {'paid_course': self.course, 'paid_lesson': self.lesson, 'payment_sum': 12000,
             'payment_method': 'BANK TRANSFER'},
            {'payment_sum': 10000, 'payment_method': 'CASH'},
        ]

        for el in payment_list:
            Payment.objects.create(**el)
