from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EMD(Timestampable):
    """
    Stores details of EMD paid by a bidder for an auction.
    """

    PS_PROCESSING = 'PR'
    PS_SUCCESS = 'S'
    PS_PENDING = 'PE'
    PS_FAILED = 'F'
    STATUS_CHOICES = [
        (PS_PROCESSING, 'Processing'),
        (PS_SUCCESS, 'Successful'),
        (PS_PENDING, 'Pending'),
        (PS_FAILED, 'Failed'),
    ]

    PM_ONLINE = 'O'
    PM_CHALLAN = 'C'
    PAYMENT_MODE_CHOICES = [
        (PM_ONLINE, 'Online'),
        (PM_CHALLAN, 'Challan'),
    ]

    auction = models.ForeignKey('hsvp.Auction', on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField(blank=True)

    processing_fees = models.DecimalField(blank=True, max_digits=7, decimal_places=2)
    total_amount = models.DecimalField(blank=True, max_digits=7, decimal_places=2)

    payment_mode = models.CharField(_('Payment mode'), choices=PAYMENT_MODE_CHOICES, max_length=5)
    status = models.CharField(_('EMD payment status'), choices=STATUS_CHOICES, max_length=5)

    def __str__(self):
        return self.processing_fees

    class Meta:
        verbose_name = _('EMD')
        verbose_name_plural = _("EMDs")
