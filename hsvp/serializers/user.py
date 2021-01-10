from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the ``User`` model.
    """
    id = serializers.IntegerField(read_only=True)

    date_joined = serializers.DateTimeField(read_only=True)
    date_invited = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        """
        # . make sure that administration level details like (is_staff, is_superuser is not being serialized)
        # . make sure that fields like is_active, date_joined, last_login are readonly
        """
        model = User
        exclude = ('is_superuser', 'is_staff', 'user_permissions', 'groups', 'is_active', 'password')


class UserPkSerializer(UserSerializer):
    """
    To be used when creating an address, for primarykey of user.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=User.objects.all()).to_internal_value(data)
