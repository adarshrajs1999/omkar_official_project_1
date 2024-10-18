# booking/models.py
from django.db import models

from django.db import models

class Couple_Room(models.Model):
    ROOM_AMOUNT_CHOICES = [
        (1000, '1000'),
        (1800, '1800'),
    ]

    Room_name = models.CharField(max_length=1000)
    Room_amount = models.IntegerField(choices=ROOM_AMOUNT_CHOICES)
    Check_in = models.DateField()
    Check_out = models.DateField()
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Adults = models.PositiveIntegerField()
    Child = models.PositiveIntegerField()


class Family_Room(models.Model):
    ROOM_AMOUNT_CHOICES = [
        (1300, '1300'),
        (2000, '2000'),
    ]

    Room_name = models.CharField(max_length=1000)
    Room_amount = models.IntegerField(choices=ROOM_AMOUNT_CHOICES)
    Check_in = models.DateField()
    Check_out = models.DateField()
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Adults = models.PositiveIntegerField()
    Child = models.PositiveIntegerField()




class Group_Room(models.Model):
    ROOM_AMOUNT_CHOICES = [
        (2000, '2000'),
        (2500, '2500'),
    ]

    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField(choices=ROOM_AMOUNT_CHOICES)
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults = models.PositiveIntegerField()
    Child = models.PositiveIntegerField()



class Six_Bed_Room(models.Model):
    ROOM_AMOUNT_CHOICES = [
        (3000, '3000'),
        (3000, '3000'),
    ]

    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField(choices=ROOM_AMOUNT_CHOICES)
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults = models.PositiveIntegerField()
    Child = models.PositiveIntegerField()

class Dormitory(models.Model):
    ROOM_AMOUNT_CHOICES = [
        (3000, '3000'),
        (3000, '3000'),
    ]

    Room_name=models.CharField(max_length=1000)
    Room_amount=models.IntegerField(choices=ROOM_AMOUNT_CHOICES)
    Check_in=models.DateField()
    Check_out=models.DateField()
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Adults = models.PositiveIntegerField()
    Child = models.PositiveIntegerField()