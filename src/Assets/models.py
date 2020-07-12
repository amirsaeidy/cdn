from django.db import models
from django_jalali.db import models as jmodels

class Time(models.Model):
    TimeExample=models.CharField(max_length=200)

    def __str__(self):
        return self.TimeExample

class Symbols(models.Model):
    Symbol_Name = models.CharField(max_length=20)
    Symbol_Id = models.CharField(max_length=20)

    def __str__(self):
        return self.Symbol_Name

class Option_Symbols(models.Model):
    Symbol_Name = models.CharField(max_length=20)
    Symbol_Id = models.IntegerField()
    Underlying_Asset= models.CharField(max_length=20) # should be in relation with another table in future
    Strike = models.IntegerField()
    Exercise_Date = models.DateField()
    Option_Types = (('P','Put'),('C','Call'))
    Option_Type = models.CharField(max_length=1,choices=Option_Types)

    def __str__(self):
        return self.Symbol_Name

class Symbols_Orders(models.Model):
    Symbol = models.ForeignKey('Symbols',on_delete=models.CASCADE,)
    # Date = models.
    # DateTime = models.

class Symbols_Transactions(models.Model):
    Symbol = models.ForeignKey('Symbols',on_delete=models.CASCADE,)
    Date=models.DateField()
    DateTime = models.DateTimeField()
    Price = models.IntegerField()
    Volume = models.IntegerField()
    Value = models.IntegerField()

    def __str__(self):
        return self.Symbol.Symbol_Name + "-" + self.Date.strftime("%Y-%m-%d")


# Create your models here.
class Future(models.Model):
    Comodity_Names = (('SA','Saffron'),('PS','Pistachio'))
    Comodity_Name =models.CharField(max_length=2,choices=Comodity_Names)

    En_DateTime=models.DateTimeField()
    Fa_DateTime=models.TextField()

    Maturity_Dates=(('ES','Esfand'),('DY','Dey'))
    Maturity_Date=models.CharField(max_length=2,choices=Maturity_Dates)

    AP1=models.IntegerField()
    AP2=models.IntegerField()
    AP3=models.IntegerField()

    BP1=models.IntegerField()
    BP2=models.IntegerField()
    BP3=models.IntegerField()

    LastDay_Settlement=models.FloatField()

    AV1=models.IntegerField()
    AV2=models.IntegerField()
    AV3=models.IntegerField()

    BV1=models.IntegerField()
    BV2=models.IntegerField()
    BV3=models.IntegerField()

    Last_Price=models.IntegerField()

    Volume_Traded=models.IntegerField()

    Open_Interest=models.IntegerField()
    
    def __str__(self):
        return self.comodity_name



