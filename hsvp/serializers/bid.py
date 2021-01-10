from rest_framework import serializers

from hsvp.models import Bid

from hsvp.serializers import BidderPkSerializer, AuctionPkSerializer

from .round import RoundPkSerializer


class BidSerializer(serializers.ModelSerializer):
    """
    Serialize for the ``Bid`` model.
    """

    id = serializers.IntegerField(read_only=True)

    auction = AuctionPkSerializer(read_only=True)

    bidder = BidderPkSerializer(read_only=True)

    round_no = RoundPkSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'
        read_only_fields = ('price', 'placed_at')
