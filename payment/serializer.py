from rest_framework import serializers
from .models import payment
class serializerpayment(serializers.ModelSerializer):
    class Meta:
        model=payment
        fields="__all__"