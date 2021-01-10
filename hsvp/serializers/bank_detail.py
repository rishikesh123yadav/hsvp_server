from rest_framework import serializers

from hsvp.models import BankDetail


class BankDetailSerializer(serializers.ModelSerializer):
    """
    Serialize for the ``BankDetail`` model.
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BankDetail
        fields = '__all__'


class BankDetailPkSerializer(BankDetailSerializer):
    """
    To be used when creating a JointHolder, for primarykey of BankDetail.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=BankDetail.objects.all()).to_internal_value(data)
