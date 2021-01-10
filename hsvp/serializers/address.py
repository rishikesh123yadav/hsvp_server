from django.contrib.auth import get_user_model

from rest_framework import serializers

from hsvp.models import Address

from hsvp.serializers import UserPkSerializer

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the ``Address`` model.
    """
    id = serializers.IntegerField(read_only=True)

    user = UserPkSerializer()

    class Meta:
        model = Address
        fields = '__all__'
