from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Subscriber
from course.paginators import CourseLessonPaginator
from course.serializers import CourseSerializer, SubscriberSerializer
from course.tasks import send_mailing
from users.permissions import IsNotModerator, IsOwner, IsSubscriber


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CourseLessonPaginator

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        if self.request.method in ['CREATE', 'DELETE', 'UPDATE']:
            self.permission_classes = [IsOwner, IsNotModerator]
        else:
            self.permission_classes = [IsOwner | IsSubscriber]
        return super(CourseViewSet, self).get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_update(self, serializer):
        serializer.save()
        sub = Subscriber.objects.get('email')
        send_mailing.delay(sub, Course)
        return super().perform_update(serializer)


class SubscriberCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class SubscriberDeleteAPIView(generics.DestroyAPIView):
    queryset = Subscriber.objects.all()
    permission_classes = [IsAuthenticated, IsSubscriber]
