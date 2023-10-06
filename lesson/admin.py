from django.contrib import admin

from lesson.models import Lesson


# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'video_link', 'course')
