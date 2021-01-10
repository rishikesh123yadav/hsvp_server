from rest_framework import serializers

from hsvp.models import JointHolder, User, BankDetail

from hsvp.serializers import BankDetailSerializer, BidderPkSerializer, UserSerializer


class JointHolderSerializer(serializers.ModelSerializer):
    """
    serializers for  ```joint holder``` .

    A bidder can add JointHolder for particular Auction .

    The number of joint holder in particular auction can be more than one .
    """
    id = serializers.IntegerField(read_only=True)

    bidder = BidderPkSerializer()

    user = UserSerializer()

    refund_account = BankDetailSerializer()

    class Meta:
        model = JointHolder
        fields = '__all__'

    def create(self, validated_data):
        bidder = validated_data.pop('bidder')
        user_data = validated_data.pop('user')
        bank_data = validated_data.pop('refund_account')
        user = User.objects.create(**user_data)
        bank_detail = BankDetail.objects.create(**bank_data)
        return JointHolder.objects.create(bidder=bidder, user=user, refund_account=bank_detail)

    def update(self, instance, validated_data):
        """
        update user and bank details from joint_holder endpoint
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
