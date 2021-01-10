from rest_framework import serializers

from hsvp.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the ``Item`` model.
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
