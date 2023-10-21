from rest_framework import serializers
from stripe.api_resources.payment_intent import PaymentIntent

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    pay = PaymentIntent.stripe_id

    class Meta:
        model = Payment
        fields = '__all__'
