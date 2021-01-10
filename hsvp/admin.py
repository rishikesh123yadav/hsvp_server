from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import (User, Bidder, BankDetail, Address,
                     Auction, AuctionDetail, AuctionDocument, Document, EMD, Item, Seller, Bid, BidderAuction, JointHolder, Round, UserDocument)


@admin.register(User)
class UserAdmin(UserAdmin):
    """
    Register User model for admin.
    """
    search_fields = ('username', 'first_name', 'last_name',
                     'email', 'contact_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
                                         'last_name', 'email', 'contact_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {
         'fields': ('last_login', 'date_joined', 'date_invited')}),
    )


@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    pass


@admin.register(AuctionDetail)
class AuctionDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(AuctionDocument)
class AuctionDocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(EMD)
class EMDAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass


@admin.register(BidderAuction)
class BidderAuction(admin.ModelAdmin):
    pass


@admin.register(JointHolder)
class JointHolderAdmin(admin.ModelAdmin):
    pass


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    pass


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    pass
