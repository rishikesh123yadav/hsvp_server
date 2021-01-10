from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BankDetail(Timestampable):
    """
    Represent Bank details independently

    All the fields are required
    """

    name = models.CharField(_('Name of account Holder'), max_length=30)

    bank_name = models.CharField(_('Full name of bank'), max_length=30)

    account_number = models.CharField(_('Account number'), max_length=30)

    ifs = models.CharField(_('IFSC code of bank'), max_length=30)

    branch = models.CharField(_('Branch name, for exam: sector 55 branch '), max_length=30)

    class Meta:
        unique_together = (('bank_name', 'account_number',),)
        verbose_name = _('bank_detail')
        verbose_name_plural = _('bank_details')

    def __str__(self):
        return self.name
