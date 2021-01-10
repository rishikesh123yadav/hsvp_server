from hsvp_server.models import Timestampable
from django.db import models
from .auction import Auction
from django.utils.translation import ugettext_lazy as _
from hsvp.models import Auction, Bidder


class Round(Timestampable):
    """
    Holds information about round which is going to be performed.
    """

    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE)
    rounds = models.IntegerField(null=True, blank=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    base_price = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2)
    h1_payment = models.ForeignKey('hsvp.Bidder', on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        verbose_name = _('round')
        verbose_name_plural = _("rounds")

    def __str__(self):
        return self.auction.name
