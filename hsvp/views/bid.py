from rest_framework.viewsets import ModelViewSet

from hsvp.models import Bid

from hsvp.serializers import BidSerializer


class BidViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Bid
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Bid.objects.all().select_related('bidder')
    serializer_class = BidSerializer
