from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from course.serializers import CourseSerializer
from users.permissions import IsNotModerator, IsOwner


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method in ['CREATE', 'DELETE']:
            self.permission_classes = [IsNotModerator]
        else:
            self.permission_classes = [IsOwner]
        return super(CourseViewSet, self).get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()
