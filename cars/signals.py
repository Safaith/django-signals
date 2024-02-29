from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Car
from buyers.models import Buyer
import uuid

@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance,**kwargs):
    print('instance: ', instance)
    if instance.code_no =="":
        instance.code_no = str(uuid.uuid4()).replace("-","").upper()[:10]
        # instance.save()

    obj = Buyer.objects.get(user=instance.buyer.user)
    # print('please: ',instance.buyer.user)
    obj.from_signal = True
    obj.save()
    