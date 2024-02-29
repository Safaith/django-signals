from django.db import models
from buyers.models import Buyer
from django.dispatch import receiver
import uuid

class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer, on_delete = models.CASCADE)
    code_no = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
    
    
    # def save(self, *args, **kwargs):
    #     if self.code_no =="":
    #         self.code_no = str(uuid.uuid4()).replace("-","").upper()[:10]
    #     return super().save(*args, **kwargs)
