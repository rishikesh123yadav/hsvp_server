from hsvp_server.models import Timestampable
from django.db import models
from .bank_detail import BankDetail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

User = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Bidder(Timestampable):
    """
    Bidder represent person who will be bidding on some item

    there can
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # in theory we must not create a bidder without refund account
    refund_account = models.OneToOneField(BankDetail, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('bidder')
        verbose_name_plural = _('bidders')

    def __str__(self):
        return self.user.first_name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{first} {last}'.format(first=self.user.first_name.capitalize(),
                                            last=self.user.last_name.capitalize())
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.user.first_name
