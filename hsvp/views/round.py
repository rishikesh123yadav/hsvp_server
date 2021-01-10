from rest_framework.viewsets import ModelViewSet

from hsvp.models import Round

from hsvp.serializers import RoundSerializer


class RoundViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Round
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Round.objects.all()
    serializer_class = RoundSerializer
