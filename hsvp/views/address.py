from rest_framework.viewsets import ModelViewSet

from hsvp.models import Address

from hsvp.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Address
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Address.objects.all().select_related('user')
    serializer_class = AddressSerializer
