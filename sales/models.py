from django.db import models
from orders.models import Order

class sales(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return str(self.amount)

