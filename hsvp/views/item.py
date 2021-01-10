from rest_framework.viewsets import ModelViewSet

from hsvp.models import Item

from hsvp.serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Item
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
