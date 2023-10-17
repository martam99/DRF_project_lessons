from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
import stripe
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

    def create_payment(self):
        stripe.api_key = "sk_test_51O1qLFBHY2SJrLQNMAVkem1Pf577FhF0uH6AG6OkOJc7sshbPCIBvtfA7Te1YH4NwGIeJng75rmtJGt2K1d2arDm008V9TmqjN"
        pay = stripe.PaymentIntent.create(
            amount=self.queryset.payment_sum,
            currency="usd",
            automatic_payment_methods={"enabled": True},
            course=self.queryset.paid_course,
            user=self.queryset.user,
            card=self.queryset.card
        )
        pay.save()

    def view_payment(self):
        stripe.api_key = "sk_test_51O1qLFBHY2SJrLQNMAVkem1Pf577FhF0uH6AG6OkOJc7sshbPCIBvtfA7Te1YH4NwGIeJng75rmtJGt2K1d2arDm008V9TmqjN"
        view_pay = stripe.PaymentIntent.retrieve(
            Payment.objects.id
        )
        view_pay.save()
        return view_pay


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'payment_method')
    ordering_fields = ['payment_date']
