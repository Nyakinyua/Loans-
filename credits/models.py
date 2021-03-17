from django.db import models
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import (pre_save,)
from django.utils.text import slugify
# Create your models here.
class Loan(models.Model):
    ProductId = models.CharField(max_length=10,default='L01')
    interestRate  = models.DecimalField(max_digits=100,decimal_places=2)

class Interest(models.Model):
    TotalInterest = models.DecimalField(max_digits=100,decimal_places=2)


class Customer(models.Model):
    custName= models.TextField(max_length=45,blank=False)
    amount=models.DecimalField(max_digits=100,decimal_places=2)
    IDNo = models.IntegerField(blank=False)
    AppDate = models.DateTimeField(auto_now_add = True)
    LInterest = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    def __str__(self):
        return self.custName
    

    @classmethod
    def get_customers(cls):
        customers=cls.objects.all()
        return customers

@receiver(pre_save, sender = Customer)
def calculate_interest(sender,instance,*args,**kwargs):
    if not instance.LInterest:
    client = Customer.objects.exclude(Loan.amount = 0.00)
    for client in client:
        R=(Loan.interestRate/100)
        LAmount=Customer.amount
        T= TimeStamp(customer.AppDate)
        instance.LInterest=Customer.objects.Create(Interest=R*LAmount*T)


    
        


  


    