from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserDocument(Timestampable):
    """
    Holds mapping of user and their related documents
    """

    user = models.ForeignKey('hsvp.User', on_delete=models.CASCADE)
    document = models.ForeignKey('hsvp.Document', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _('user details')
        verbose_name_plural = _("users' details")
        unique_together = (
            ('user', 'document')
        )
