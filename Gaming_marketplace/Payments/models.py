from django.db import models

# Create your models here.
class Payment(models.Model):
    username = models.CharField(max_length=50)
    amount_money = models.IntegerField()
    comment = models.TextField(blank=True)