from rest_framework.viewsets import ModelViewSet

from hsvp.models import Bidder

from hsvp.serializers import BidderSerializer


class BidderViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Bidder
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Bidder.objects.all().select_related('user')
    serializer_class = BidderSerializer
