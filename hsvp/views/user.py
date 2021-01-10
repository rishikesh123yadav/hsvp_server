from rest_framework.viewsets import ModelViewSet

from hsvp.models import User

from hsvp.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    APIs to perform CRUD on User
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
