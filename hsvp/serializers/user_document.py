from rest_framework import serializers

from hsvp.models import UserDocument

from hsvp.serializers import UserPkSerializer

from hsvp.serializers import DocumentPkSerializer


class UserDocumentSerializer(serializers.ModelSerializer):
    """
    Serialize for UserDocuments.
    """

    id = serializers.IntegerField(read_only=True)

    user = UserPkSerializer()

    document = DocumentPkSerializer()

    class Meta:
        model = UserDocument
        fields = '__all__'
