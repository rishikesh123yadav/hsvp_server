from rest_framework import serializers

from hsvp.models import Document

from django.conf import settings


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serialize for the ``Documents`` model.
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'


class DocumentPkSerializer(DocumentSerializer):
    """
    To be used when creating a UserDocument, for primarykey of Document.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=Document.objects.all()).to_internal_value(data)
