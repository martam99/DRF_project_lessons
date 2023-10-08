from django.db import models

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
