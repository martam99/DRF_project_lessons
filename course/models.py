from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', default='no photo')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    start_date = models.DateTimeField(verbose_name='дата подписки', default=timezone.now())
    is_subscribed = models.BooleanField(verbose_name='статус', default=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user}{self.course}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
