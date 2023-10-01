from django.db import models

from users.models import NULLABLE


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='lessons/', verbose_name='фото', default='no lesson photo')
    video_link = models.CharField(max_length=150, verbose_name='ссылка', **NULLABLE)

    def __str__(self):
        return f'{self.title},{self.description}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
