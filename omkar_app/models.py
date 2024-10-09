# booking/models.py
from django.db import models



class Couple_Room(models.Model):
    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField()
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults=models.IntegerField()
    Child=models.IntegerField()

class Family_Room(models.Model):
    Room_name = models.CharField(max_length=1000)
    Room_amount = models.IntegerField()
    Check_in = models.DateField()
    Check_out = models.DateField()
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Adults = models.IntegerField()
    Child = models.IntegerField()

class Group_Room(models.Model):
    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField()
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults=models.IntegerField()
    Child=models.IntegerField()

class Six_Bed_Room(models.Model):
    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField()
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults=models.IntegerField()
    Child=models.IntegerField()

class Dormitory(models.Model):
    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField()
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults=models.IntegerField()
    Child=models.IntegerField()