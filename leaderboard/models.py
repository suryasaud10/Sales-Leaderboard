from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

# Create your models here.

class SalesRecord(models.Model):
    agent_name = models.CharField(max_length=100, db_index=True)
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deals_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['agent_name']),
        ]
    def __str__(self):
        return f"{self.agent_name} - {self.sales_amount} - {self.deals_count}"  

