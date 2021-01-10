from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Item(Timestampable):

    name = models.CharField(_('Name of item that will be auctioned'), max_length=300)
    description = models.TextField(blank=True, null=True)
    image_url = models.CharField(blank=True, null=True, max_length=100)
    auction_detail = models.ForeignKey('hsvp.AuctionDetail', on_delete=models.CASCADE, null=True, blank=True, related_name='auction_items')

    class Meta:

        verbose_name = _('item')
        verbose_name_plural = _('items')

    def __str__(self):
        return self.auction_detail.name
