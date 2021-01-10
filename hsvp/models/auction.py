from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Auction(Timestampable):
    """
    Auction data:
    - registration date, payment amount (EMD),
    - when does it start, end
    - when does its winning bids' final payment date is, what the winning bids' payment percent is
    - auction details - of the auctionable items - in AuctionDetail
    - starting price from round 1 - base_price
    """

    seller = models.ForeignKey(
        'hsvp.Seller', blank=True, null=True, on_delete=models.SET_NULL)

    name = models.CharField(_('Auction name'), max_length=300)
    description = models.TextField(blank=True)

    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

    no_of_rounds = models.PositiveSmallIntegerField(blank=True)

    # we can store upto 1000cr base price
    base_price = models.DecimalField(blank=True, max_digits=13, decimal_places=2)

    registration_time_starts_at = models.DateTimeField(null=True, blank=True)
    registration_time_ends_at = models.DateTimeField(null=True, blank=True)

    # we can store upto 9 lacs
    emd_amount = models.DecimalField(blank=True, max_digits=7, decimal_places=2)
    h1_payment_percent = models.DecimalField(blank=True, max_digits=4, decimal_places=2)
    h1_payment_end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('auction')
        verbose_name_plural = _("auctions")

    def __str__(self):
        return self.name
