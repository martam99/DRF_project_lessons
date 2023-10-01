from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LessonConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk/', LessonRetrieveAPIView.as_view(), name='lesson-view'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]
