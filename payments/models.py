from django.db import models
from django.utils.timezone import now as now

from course.models import Course
from lesson.models import Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Payment(models.Model):
    METHOD = (
        ('CASH', 'наличные'),
        ('BANK TRANSFER', 'перевод на счет')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(verbose_name='дата оплаты', default=now)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс,', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты', **NULLABLE)
    payment_method = models.CharField(max_length=30, verbose_name='способ оплаты', choices=METHOD)
    card = models.CharField(max_length=30, verbose_name='номер карты', default='no card')
    objects = models.Manager()

    def __str__(self):
        return f'{self.payment_sum},{self.payment_method}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
