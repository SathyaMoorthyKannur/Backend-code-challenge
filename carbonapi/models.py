
from django.db import models
from django.forms import FloatField

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Usage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    usage_type_id = models.BigIntegerField()
    usage_at = models.DateTimeField()
    date_created = models.DateField()
    amount = models.FloatField()

class Usage_types(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    factor = models.FloatField()



