"""
All base classes for models should be here
"""
from django.db import models


class Timestampable(models.Model):
    """
    Some entities need to keep record of the time when they were created/modified.
    """
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_on = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
