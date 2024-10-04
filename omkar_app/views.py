# booking/views.py
from django.shortcuts import render, redirect
from .forms import AvailabilityForm, BookingForm

from .models import Room

def home(request):
    return render(request,'home.html')

def background(request):
    return render(request,'background.html')

def check_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            room_type = form.cleaned_data['room_type']
            is_ac = form.cleaned_data['is_ac']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            room = Room.objects.filter(room_type=room_type, is_ac=is_ac, available=True).first()

            if room:
                return render(request, 'available.html', {'room': room})
            else:
                return redirect('not_available')
    else:
        form = AvailabilityForm()

    return render(request, 'check_availability.html', {'form': form})


def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('payment_options')
    else:
        form = BookingForm()

    return render(request, 'book_room.html', {'form': form, 'room': room})


def payment_options(request):
    return render(request, 'payment_options.html')


def cash_payment(request):
    return render(request,'cash_booking_confirmed.html')




# booking/views.py
from django.shortcuts import render, redirect
from django.conf import settings
import razorpay

def online_payment(request):
    if request.method == 'POST':
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': 1000, 'currency': 'INR', 'payment_capture': '1'})
        return render(request, 'razorpay_payment.html', {'payment': payment})

    return render(request, 'razorpay_payment.html')

def payment_success(request):
    payment_id = request.GET.get('payment_id')
    # Process the payment_id as needed (e.g., store it in the database)
    return render(request, 'payment_success.html', {'payment_id': payment_id})

def not_available(request):
    return render(request,'not_available.html')



