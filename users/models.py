from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class UserRole(models.TextChoices):
    MODERATOR = 'moderator'
    MEMBER = 'member'


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, verbose_name='Почта', unique=True)
    phone = models.IntegerField(verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото', default='no photo')
    is_active = models.BooleanField(default=True, verbose_name='activity')
    role = models.CharField(max_length=30, verbose_name='role', choices=UserRole.choices, default='member')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
