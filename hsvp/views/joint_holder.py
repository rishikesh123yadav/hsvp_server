from rest_framework.viewsets import ModelViewSet

from hsvp.models import JointHolder

from hsvp.serializers import JointHolderSerializer


class JointHolderViewSet(ModelViewSet):
    """
    APIs to perform CRUD on JointHolder
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = JointHolder.objects.all()
    serializer_class = JointHolderSerializer
