from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
import stripe
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import Payment
from payments.serializers import PaymentSerializer


# Create your views here.


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.save()
        return super().perform_create(serializer)


class PaymentCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        """Метод для создания объекта PaymentIntent"""
        payment = serializer.save()
        stripe.api_key = "sk_test_51O1qLFBHY2SJrLQNMAVkem1Pf577FhF0uH6AG6OkOJc7sshbPCIBvtfA7Te1YH4NwGIeJng75rmtJGt2K1d2arDm008V9TmqjN"
        pay = stripe.PaymentIntent.create(
            amount=payment.payment_sum,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()
        return super().perform_create(serializer)


class GetPaymentView(APIView):
    """Получение информации о платеже."""
    def get(self, request, payment_id):
        """Метод для получения информации о платеже"""
        stripe.api_key = "sk_test_51O1qLFBHY2SJrLQNMAVkem1Pf577FhF0uH6AG6OkOJc7sshbPCIBvtfA7Te1YH4NwGIeJng75rmtJGt2K1d2arDm008V9TmqjN"
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status,
            'body': payment_intent})


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'payment_method')
    ordering_fields = ['payment_date']
