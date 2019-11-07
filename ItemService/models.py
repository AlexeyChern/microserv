from django.db import models

# Create your models here.
class item (models.Model):
    itemID = models.AutoField(primary_key=True)
    Name = models.TextField(max_length=255)
    Price = models.FloatField()
    Amount = models.IntegerField()
