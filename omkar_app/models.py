# booking/models.py
from django.db import models


class Room(models.Model):
    ROOM_CHOICES = [
        ('double_bed', 'Double Bed Room'),
        ('triple_bed', 'Triple Bed Room'),
        ('four_bed', '4 Bed Room'),
        ('dormitory', 'Dormitory')
    ]

    room_type = models.CharField(choices=ROOM_CHOICES, max_length=20)
    is_ac = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.get_room_type_display()} - {'AC' if self.is_ac else 'Non-AC'}"


class Booking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 2000,null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def _str_(self):
        return f"Booking for {self.name} - {self.room}"


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