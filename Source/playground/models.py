from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    acc_num = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    balance = models.FloatField()

    
class Card(models.Model):
    card_num = models.AutoField(primary_key=True)
    account_num = models.ForeignKey(Account, on_delete = models.SET_NULL,null=True)
    pin = models.IntegerField(max_length=10)
    issue_date= models.DateField()
    expiry_date = models.DateField()
    card_status = models.CharField(max_length=10)


class Machine(models.Model):
    machine_id=models.AutoField(primary_key=True)
    current_balance = models.FloatField()
    location = models.TextField()
    minimum_balance = models.FloatField()
    last_refill = models.DateTimeField()
    next_maintenance_date = models.DateField()

    
class Transaction(models.Model):
    Transaction_id = models.AutoField(primary_key=True)
    card_num = models.ForeignKey(Card,on_delete = models.SET_NULL,null=True)
    machine_id = models.ForeignKey(Machine,on_delete = models.SET_NULL,null=True)
    date_time=models.DateTimeField()
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=50)



