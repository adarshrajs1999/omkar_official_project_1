# booking/forms.py
from email.headerregistry import Group

from django import forms
from .models import  Couple_Room, Family_Room, Group_Room, Six_Bed_Room, Dormitory



class ValidationError:
    pass


class CoupleRoomForm(forms.ModelForm):
    class Meta:
        model = Couple_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name','value':'Couple Room','readonly':'readonly'}),
            'Room_amount': forms.Select(attrs={'class': 'form-control'},choices=[(1000, '1000'), (1800, '1800')] ),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            check_in = cleaned_data.get('Check_in')
            check_out = cleaned_data.get('Check_out')

            if check_in and check_out and check_in >= check_out:
                raise ValidationError('Check-out date must be after check-in date.')

            return cleaned_data


class FamilyRoomForm(forms.ModelForm):
    class Meta:
        model = Family_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name','value':'Family Room','readonly':'readonly'}),
            'Room_amount': forms.Select(attrs={'class': 'form-control'},choices=[(1300, '1300'), (2000, '2000')]),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            check_in = cleaned_data.get('Check_in')
            check_out = cleaned_data.get('Check_out')

            if check_in and check_out and check_in >= check_out:
                raise ValidationError('Check-out date must be after check-in date.')

            return cleaned_data




class GroupRoomForm(forms.ModelForm):
    class Meta:
        model = Group_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name','value':'Group Room','readonly':'readonly'}),
            'Room_amount': forms.Select(attrs={'class': 'form-control'},choices=[(2000, '2000'), (2500, '2500')]),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            check_in = cleaned_data.get('Check_in')
            check_out = cleaned_data.get('Check_out')

            if check_in and check_out and check_in >= check_out:
                raise ValidationError('Check-out date must be after check-in date.')

            return cleaned_data






class SixBedRoomForm(forms.ModelForm):
    class Meta:
        model = Six_Bed_Room  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name','value':'Six Bed Room','readonly':'readonly'}),
            'Room_amount': forms.Select(attrs={'class': 'form-control'},choices=[(3000, '3000'), (3000, '3000')]),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            check_in = cleaned_data.get('Check_in')
            check_out = cleaned_data.get('Check_out')

            if check_in and check_out and check_in >= check_out:
                raise ValidationError('Check-out date must be after check-in date.')

            return cleaned_data




class DormitoryForm(forms.ModelForm):
    class Meta:
        model = Dormitory  # Link the form to the Couple_Room model
        fields = '__all__'  # Use all fields in the model, or you can specify certain fields like ['Room_name', 'Room_amount', ...]

        # Add customizations to widgets if necessary
        widgets = {
            'Room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Name','value':'Dormitory','readonly':'readonly'}),
            'Room_amount': forms.Select(attrs={'class': 'form-control'},choices=[(3000, '3000'), (3000, '30000')]),
            'Check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'Adults': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Adults'}),
            'Child': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Children'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            check_in = cleaned_data.get('Check_in')
            check_out = cleaned_data.get('Check_out')

            if check_in and check_out and check_in >= check_out:
                raise ValidationError('Check-out date must be after check-in date.')

            return cleaned_data


