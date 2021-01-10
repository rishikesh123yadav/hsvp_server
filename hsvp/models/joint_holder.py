from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class JointHolder(Timestampable):
    """
    A user can add a joint holder here .

    who perform the bidding process in absence of user.
    """
    bidder = models.ForeignKey('hsvp.Bidder', on_delete=models.CASCADE)
    user = models.ForeignKey('hsvp.User', on_delete=models.CASCADE)
    refund_account = models.ForeignKey('hsvp.BankDetail', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('joint holder')
