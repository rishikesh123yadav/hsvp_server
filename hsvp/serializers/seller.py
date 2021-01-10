from rest_framework import serializers

from hsvp.models import Seller, User, BankDetail

from hsvp.serializers import UserSerializer

from hsvp.serializers import BankDetailSerializer


class SellerSerializer(serializers.ModelSerializer):
    """
    Serialize the relation between ``User`` and ``Seller (User)``.
    """
    id = serializers.IntegerField(read_only=True)

    user = UserSerializer()

    primary_account = BankDetailSerializer()

    class Meta:
        model = Seller
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        bank_data = validated_data.pop('primary_account')
        user = User.objects.create(**user_data)
        bank_detail = BankDetail.objects.create(**bank_data)
        return Seller.objects.create(user=user, primary_account=bank_detail)

    def update(self, instance, validated_data):
        """
        update user and bank details from seller endpoint
        """
        user_data = validated_data.pop('user')
        bank_data = validated_data.pop('primary_account')

        if user_data:
            user = UserSerializer(instance.user, user_data)
            user.is_valid(raise_exception=True)
            user.save()

        if bank_data:
            bank_detail = BankDetailSerializer(instance.primary_account, bank_data)
            bank_detail.is_valid(raise_exception=True)
            bank_detail.save()

        return instance


class AuctionSellerSerializer(SellerSerializer):
    """
    To be used when creating an auction for primarykey of seller.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all()).to_internal_value(data)
