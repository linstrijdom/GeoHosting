# serializers.py
from django.utils.timezone import localtime
from rest_framework import serializers

from geohosting.models.subscription import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Subscription serializer."""

    current_period_start = serializers.SerializerMethodField()
    current_period_end = serializers.SerializerMethodField()
    current_expiry_at = serializers.SerializerMethodField()
    is_waiting_payment = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = '__all__'

    def get_current_period_start(self, obj: Subscription):
        """Return current_period_start."""
        return localtime(obj.current_period_start).strftime(
            '%Y-%m-%d %H:%M:%S %Z'
        )

    def get_current_period_end(self, obj: Subscription):
        """Return current_period_end."""
        return localtime(obj.current_period_end).strftime(
            '%Y-%m-%d %H:%M:%S %Z'
        )

    def get_current_expiry_at(self, obj: Subscription):
        """Return current_expiry_at."""
        return localtime(obj.current_expiry_at).strftime(
            '%Y-%m-%d %H:%M:%S %Z'
        )

    def get_is_waiting_payment(self, obj: Subscription):
        """Return is is_waiting_payment."""
        return obj.is_waiting_payment


class SubscriptionDetailSerializer(SubscriptionSerializer):
    """Subscription detail serializer."""

    detail = serializers.SerializerMethodField()

    def get_detail(self, obj: Subscription):
        """Return is detail."""
        obj.update_payment()
        return obj.detail
