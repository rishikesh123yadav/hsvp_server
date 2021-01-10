from rest_framework.viewsets import ModelViewSet

from hsvp.models import BankDetail

from hsvp.serializers import BankDetailSerializer


class BankDetailViewSet(ModelViewSet):
    """
    APIs to perform CRUD on bank_detail
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
