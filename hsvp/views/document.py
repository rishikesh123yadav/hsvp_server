from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from hsvp.models import Document

from hsvp.serializers import DocumentSerializer

from rest_framework.parsers import MultiPartParser, FormParser


class DocumentViewSet(ModelViewSet):
    """
    APIs to perform CRUD on Document
    for now allowing all CRUD on this entity in future may want to allow selected operations
    """
    queryset = Document.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
