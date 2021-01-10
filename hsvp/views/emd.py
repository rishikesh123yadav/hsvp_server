from rest_framework.viewsets import ModelViewSet

from hsvp.models import EMD

from hsvp.serializers import EMDSerializer


class EMDViewSet(ModelViewSet):
    """
    APIs to perform CRUD on EMD
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = EMD.objects.all().select_related('auction')
    serializer_class = EMDSerializer
