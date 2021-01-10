from rest_framework import serializers

from hsvp.models import Auction, Document, AuctionDocument

from hsvp.serializers import DocumentPkSerializer, AuctionPkSerializer


class AuctionDocumentSerializer(serializers.ModelSerializer):
    """
    Serialize for the ``Auction Document`` model.
    """
    id = serializers.IntegerField(read_only=True)

    auction = AuctionPkSerializer()

    document = DocumentPkSerializer()

    class Meta:
        model = AuctionDocument
        fields = '__all__'
