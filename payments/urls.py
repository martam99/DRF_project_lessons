from django.urls import path
from rest_framework.routers import DefaultRouter

from payments.apps import PaymentsConfig
from payments.views import PaymentViewSet, PaymentListAPIView

app_name = PaymentsConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
                  path('list/', PaymentListAPIView.as_view(), name='payment-list')
              ] + router.urls
