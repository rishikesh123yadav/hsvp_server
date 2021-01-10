from rest_framework import serializers

from hsvp.models import Auction, AuctionDetail, Document, Item

from hsvp.serializers import AuctionSellerSerializer, DocumentSerializer, AuctionDetailSerializer


class AuctionSerializer(serializers.ModelSerializer):
    """
    Serializer for the ``Auction`` model.

    ``AuctionDetail`` also will create when ``Auction`` serialized.

    ``Document`` also will create when ``Auction`` serialized.

    """
    id = serializers.IntegerField(read_only=True)

    seller = AuctionSellerSerializer()

    documents = DocumentSerializer(many=True)

    details = AuctionDetailSerializer()

    class Meta:
        model = Auction
        fields = ['id', 'name', 'description', 'starts_at', 'ends_at', 'seller', 'no_of_rounds', 'base_price', 'registration_time_starts_at', 'registration_time_ends_at', 'emd_amount', 'h1_payment_percent', 'h1_payment_end_date', 'documents', 'details']  # , 'auction_items']

    def create(self, validated_data):
        document_data = validated_data.pop('documents', None)
        auction_detail = validated_data.pop('details', None)
        items = auction_detail.pop('auction_items', None)
        auction = Auction.objects.create(**validated_data)
        if document_data is not None:
            for doc_data in document_data:
                Document.objects.create(**doc_data, auction=auction)
        auction_detail = AuctionDetail.objects.create(**auction_detail, auction=auction)
        if items is not None:
            for item in items:
                Item.objects.create(**item, auction_detail=auction_detail)
        print(auction)
        return auction

    def update(self, instance, validated_data):
        """
        update auction,auction_detail and auction_document details from auction endpoint
        """

        instance.seller = validated_data.get('seller', instance.seller)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.starts_at = validated_data.get('starts_at', instance.starts_at)
        instance.ends_at = validated_data.get('ends_at', instance.ends_at)
        instance.no_of_rounds = validated_data.get('no_of_rounds', instance.no_of_rounds)
        instance.base_price = validated_data.get('base_price', instance.base_price)
        instance.registration_time_starts_at = validated_data.get('registration_time_starts_at', instance.registration_time_starts_at)
        instance.registration_time_ends_at = validated_data.get('registration_time_ends_at', instance.registration_time_ends_at)
        instance.emd_amount = validated_data.get('emd_amount', instance.emd_amount)
        instance.h1_payment_percent = validated_data.get('h1_payment_percent', instance.h1_payment_percent)
        instance.h1_payment_end_date = validated_data.get('h1_payment_end_date', instance.h1_payment_end_date)
        instance.save()

        return instance


class AuctionPkSerializer(AuctionSerializer):
    """
    To be used when creating a related serializers, for primarykey of Auction.
    """

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField(queryset=Auction.objects.all()).to_internal_value(data)
