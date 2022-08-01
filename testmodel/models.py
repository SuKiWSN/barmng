from django.db import models

# Create your models here.
from django.db import models


class clients(models.Model):
    address = models.CharField(max_length=20, default=False)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default=False)
    assets = models.IntegerField()
    regdata = models.IntegerField()
    rank = models.IntegerField()
    role = models.IntegerField()
    gend = models.CharField(max_length=2)

class vertify(models.Model):
    address = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    time = models.IntegerField()

class recharge(models.Model):
    address = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    money = models.IntegerField()
    date = models.IntegerField()

class usr_cost(models.Model):
    address = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    date = models.IntegerField()