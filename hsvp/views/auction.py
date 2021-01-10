from rest_framework.viewsets import ModelViewSet

from hsvp.models import Auction

from hsvp.serializers import AuctionSerializer


class AuctionViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Auction
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Auction.objects.all().select_related('seller')
    serializer_class = AuctionSerializer
