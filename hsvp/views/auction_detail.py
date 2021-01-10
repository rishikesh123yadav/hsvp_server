from rest_framework.viewsets import ModelViewSet

from hsvp.models import AuctionDetail

from hsvp.serializers import AuctionDetailSerializer


class AuctionDetailViewSet(ModelViewSet):
    """
    APIs to perform CRUD on auction_detail
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = AuctionDetail.objects.all()
    serializer_class = AuctionDetailSerializer
