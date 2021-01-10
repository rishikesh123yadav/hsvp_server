from rest_framework import serializers

from hsvp.models import AuctionDetail, Item

#from hsvp.serializers import ItemSerializer


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the ``Item`` model.
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class AuctionDetailSerializer(serializers.ModelSerializer):
    """
    Serialize for the ``AuctionDetail`` model.
    """
    id = serializers.IntegerField(read_only=True)

    auction_items = ItemSerializer(many=True)

    class Meta:
        model = AuctionDetail
        fields = ['id', 'name', 'description', 'quantity', 'auction_items']
