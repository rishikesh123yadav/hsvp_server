from rest_framework.viewsets import ModelViewSet

from hsvp.models import AuctionDocument

from hsvp.serializers import AuctionDocumentSerializer


class AuctionDocumentViewSet(ModelViewSet):
    """
    APIs to perform CRUD on auction_document
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = AuctionDocument.objects.all().select_related('auction')
    serializer_class = AuctionDocumentSerializer
