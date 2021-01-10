from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AuctionDetail(Timestampable):
    """
    Holds information about the items that will be auctioned in an auction.
    Eg., how much quantity of the item to be auctioned will be there.
    Other details, etc.
    """

    # TODO - do following two fields make sense? They're already there in Item
    name = models.CharField(_('Name of auctionable item'), max_length=300)
    description = models.TextField(blank=True)
    quantity = models.PositiveSmallIntegerField(blank=True)
    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE, null=True, blank=True, related_name='details')

    class Meta:
        verbose_name = _('auction details')
        verbose_name_plural = _("auctions' details")

    def __str__(self):
        return self.name
