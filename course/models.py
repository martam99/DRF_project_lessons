from django.db import models


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', default='no photo')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
