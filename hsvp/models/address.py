from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hsvp_server.choices import address_types
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

User = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Address(Timestampable):
    """
    Represent Address of an entity
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.CharField(_('Type of address'), max_length=30, choices=address_types)
    line_1 = models.CharField(_('Address line 1'), max_length=90)
    line_2 = models.CharField(_('Address line 2'), max_length=90, blank=True, null=True)

    pincode = models.CharField(_('6 Digit pincode'), max_length=10)

    state = models.CharField(_('State'), max_length=30)
    city = models.CharField(_('City'), max_length=30)
    country = models.CharField(_('Country'), max_length=30)

    contact_number = PhoneNumberField(
        verbose_name=_('contact number'),
        null=True, default=None,
    )

    notes = models.TextField(_('Any notes associated with particular address'), blank=True, null=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return self.user.first_name
