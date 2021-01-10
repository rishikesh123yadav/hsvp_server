from hsvp_server.models import Timestampable
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .bidder import Bidder
from .round import Round
from .auction import Auction


class Bid(Timestampable):
    """
    Bidder can bid on particular item here.
    """

    bidder = models.ForeignKey('hsvp.Bidder', on_delete=models.CASCADE)
    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE)
    round_no = models.ForeignKey('hsvp.Round', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=13, null=True, blank=True, decimal_places=2)
    placed_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('bid')
        verbose_name_plural = _("bids")
