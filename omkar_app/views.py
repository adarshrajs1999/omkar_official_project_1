from django.shortcuts import render, redirect
from .forms import BookingForm
from django.conf import settings
import razorpay

from .models import Booking


def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Set a fixed amount for simplicity (you can make it dynamic)
            booking.amount = 1000.00
            booking.save()
            # Redirect to the payment page
            return redirect('payment', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def payment_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment_order = client.order.create({
        'amount': int(booking.amount * 100),  # Amount in paise
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'booking': booking,
        'order_id': payment_order['id'],
        'amount': booking.amount
    }

    return render(request, 'payment.html', context)

def payment_success(request):
    return render(request, 'success.html')


