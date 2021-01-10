from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from hsvp.models import Auction, Round


@receiver(post_save, sender=Auction)
def create_round(sender, instance, created, **kwargs):
    """
    It will create a round object automatically when an Auction will generated.
    """

    if created:
        for i in range(instance.no_of_rounds):
            Round.objects.create(auction=instance, rounds=i + 1)
