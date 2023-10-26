from rest_framework import serializers
from course.models import Course, Subscriber
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)
    subscriber = SubscriberSerializer(source='subscriber_set', read_only=True, many=True)

    def get_lesson_count(self, obj):
        obj = Lesson.objects.all()
        return obj.count()

    class Meta:
        model = Course
        fields = ['title', 'description', 'preview', 'lesson_count', 'lessons', 'subscriber']
