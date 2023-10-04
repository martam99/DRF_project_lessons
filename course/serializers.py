from rest_framework import serializers
from course.models import Course
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    def get_lesson_count(self, obj):
        obj = Lesson.objects.all()
        return obj.count()

    class Meta:
        model = Course
        fields = ['title', 'description', 'lessons', 'lesson_count']
