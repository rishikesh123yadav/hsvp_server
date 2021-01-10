from rest_framework import serializers

from hsvp.models import EMD

from hsvp.serializers import AuctionPkSerializer


class EMDSerializer(serializers.ModelSerializer):
    """
    serializers for the ``EMD`` model.
    """
    id = serializers.IntegerField(read_only=True)

    auction = AuctionPkSerializer()

    class Meta:
        model = EMD
        fields = '__all__'
