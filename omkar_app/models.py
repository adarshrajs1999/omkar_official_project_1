from django.db import models

class Booking(models.Model):
    ROOM_CHOICES = (
        ('Single', 'Single Room'),
        ('Double', 'Double Room'),
        ('Suite', 'Suite Room'),
        ('Deluxe', 'Deluxe Room'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    room_type = models.CharField(choices=ROOM_CHOICES, max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.name} - {self.room_type}"