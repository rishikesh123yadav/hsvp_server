from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AuctionDocument(Timestampable):
    """
    Holds mapping of auction and its related documents.
    """

    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE)
    document = models.ForeignKey('hsvp.Document', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _('auction documents')
        verbose_name_plural = _("auctions' documents")
        unique_together = (
            ('auction', 'document'),
        )