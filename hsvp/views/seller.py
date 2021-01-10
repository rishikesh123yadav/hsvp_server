from rest_framework.viewsets import ModelViewSet

from hsvp.models import Seller

from hsvp.serializers import SellerSerializer


class SellerViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Seller
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Seller.objects.all().select_related('user')
    serializer_class = SellerSerializer
