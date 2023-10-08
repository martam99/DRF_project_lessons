from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lesson.models import Lesson
from lesson.serializers import LessonSerializer
from users.permissions import IsNotModerator, IsOwner


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsNotModerator]

    def perform_create(self, serializer):
        lesson = serializer.save
        lesson.owner = self.request.user
        lesson.save(
        )


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsNotModerator]

