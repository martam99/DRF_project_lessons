from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Subscriber


@shared_task
def send_mailing(pk, model):
    send_mail(
        subject=f'Обновление курса',
        message='Курс, на который вы подписаны обновился. Предлагаем посмотреть обновление на нашем сайте .',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[pk]
    )