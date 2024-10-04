# booking/forms.py
from django import forms
from .models import Room, Booking


class AvailabilityForm(forms.Form):
    ROOM_CHOICES = [
        ('double_bed', 'Double Bed Room'),
        ('triple_bed', 'Triple Bed Room'),
        ('four_bed', 'Four Bed Room'),
        ('dormitory', 'Dormitory')
    ]

    room_type = forms.ChoiceField(choices=ROOM_CHOICES)
    is_ac = forms.ChoiceField(choices=[(True, 'AC'), (False, 'Non-AC')])
    check_in = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'address', 'phone', 'email','check_in','check_out']