from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hsvp.models import Bidder, Auction, EMD


class BidderAuction(Timestampable):
    """
    Stores the mapping of bidder, the auction he participated in, and the EMD he paid for entering it
    """

    bidder = models.ForeignKey('hsvp.Bidder', on_delete=models.CASCADE)
    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE)
    emd = models.ForeignKey('hsvp.Emd', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('bidder auction')
        verbose_name_plural = _("bidders' auction")
        unique_together = (
            ('bidder', 'auction'),
        )
