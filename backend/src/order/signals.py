from django.db.models.signals import pre_delete

from .models import Order


def deleteConsigneeProfile(sender, instance, *args, **kwargs):
    profile = instance.consignee

    if profile:
        profile.delete()


pre_delete.connect(deleteConsigneeProfile, sender=Order)
