from rest_framework import serializers

from hsvp.models import Round

from hsvp.serializers import AuctionPkSerializer

from hsvp.serializers import BidderPkSerializer


class RoundSerializer(serializers.ModelSerializer):
    """
    serializers for the ``round`` model.
    """

    id = serializers.IntegerField(read_only=True)

    auction = AuctionPkSerializer()

    h1_payment = BidderPkSerializer()

    class Meta:
        model = Round
        fields = '__all__'


class RoundPkSerializer(RoundSerializer):
    """
    To be used when creating a bid for primarykey of Round.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=Round.objects.all()).to_internal_value(data)
