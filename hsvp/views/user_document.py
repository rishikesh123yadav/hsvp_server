from rest_framework.viewsets import ModelViewSet

from hsvp.models import UserDocument

from hsvp.serializers import UserDocumentSerializer


class UserDocumentViewSet(ModelViewSet):
    """
    APIs to perform CRUD on UserDocument
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = UserDocument.objects.all().select_related('user')
    serializer_class = UserDocumentSerializer
