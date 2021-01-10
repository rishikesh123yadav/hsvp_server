from rest_framework import serializers

from hsvp.models import Bidder, User, BankDetail

from hsvp.serializers import UserSerializer

from hsvp.serializers import BankDetailSerializer


class BidderSerializer(serializers.ModelSerializer):
    """
    Serialize the relation between ``User`` and ``Bidder (User)``.
    """
    id = serializers.IntegerField(read_only=True)

    user = UserSerializer()

    refund_account = BankDetailSerializer()

    class Meta:
        model = Bidder
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        bank_data = validated_data.pop('refund_account')
        user = User.objects.create(**user_data)
        bank_detail = BankDetail.objects.create(**bank_data)
        return Bidder.objects.create(user=user, refund_account=bank_detail)

    def update(self, instance, validated_data):
        """
        update user and bank details from Bidder endpoint
        """
        user_data = validated_data.pop('user')
        bank_data = validated_data.pop('refund_account')

        if user_data:
            user = UserSerializer(instance.user, user_data)
            user.is_valid(raise_exception=True)
            user.save()

        if bank_data:
            bank_detail = BankDetailSerializer(instance.refund_account, bank_data)
            bank_detail.is_valid(raise_exception=True)
            bank_detail.save()

        return instance


class BidderPkSerializer(BidderSerializer):
    """
    To be used when creating a related  serializers, for primarykey of bidder.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=Bidder.objects.all()).to_internal_value(data)
