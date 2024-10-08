# booking/forms.py
from email.headerregistry import Group

from django import forms
from .models import Room, Booking, Couple_Room, Family_Room, Group_Room, Six_Bed_Room, Dormitory


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
    check_in = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['name', 'address', 'phone', 'email','check_in','check_out']


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Couple_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name'}),
            'Room_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Amount'}),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Family_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name'}),
            'Room_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Amount'}),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Group_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name'}),
            'Room_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Amount'}),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Six_Bed_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name'}),
            'Room_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Amount'}),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Dormitory  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name'}),
            'Room_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Amount'}),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }
