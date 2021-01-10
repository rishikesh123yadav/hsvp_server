from hsvp_server.models import Timestampable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(Timestampable):
    """
    Holds mapping of auction and its related documents.
    """

    name = models.CharField(_('Document name'), max_length=300)

    # todo - should this be a choice field? do we have a preset of choices?
    doc_type = models.CharField(_('Document type'), max_length=300, blank=True, null=True)

    file_url_1 = models.CharField(_('Document_Image_1'), default='posts/default.jpg', max_length=100)
    file_url_2 = models.CharField(_('Document_Image_2'), default='posts/default.jpg', max_length=100)
    auction = models.ForeignKey('hsvp.Auction', on_delete=models.RESTRICT, null=True, blank=True, related_name='documents')

    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _("documents")

    def __str__(self):
        return self.name
