from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import sales
from orders.models import Order

@receiver(pre_delete, sender=sales)
def pre_delete_is_active(sender, instance, **kwargs):
    obj = instance.order
    obj.is_active = False
    