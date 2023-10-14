from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CourseViewSet, SubscriberCreateAPIView, SubscriberDeleteAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('create', SubscriberCreateAPIView.as_view(), name='subscribers-create'),
    path('delete/<int:pk>/', SubscriberDeleteAPIView.as_view(), name='subscribers-delete'),
]+router.urls
