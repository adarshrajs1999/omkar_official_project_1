# booking/views.py
from django.shortcuts import render, redirect
from .forms import  CoupleRoomForm, FamilyRoomForm, GroupRoomForm, DormitoryForm, \
    SixBedRoomForm
from django.conf import settings
import razorpay



def home(request):
    return render(request,'home.html')

def background(request):
    return render(request,'background.html')





def payment_options(request):
    return render(request, 'payment_options.html')


def cash_payment(request):
    return render(request,'cash_booking_confirmed.html')




# booking/views.py


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

def book_couple_room(request):
    if request.method == 'POST':
        form = CoupleRoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Couple_Room model
            return redirect('booking-success')  # Redirect to the success page
    else:
        form = CoupleRoomForm()

    return render(request, 'Couple.html', {'form': form})



def book_Family_room(request):
    if request.method == 'POST':
        form = FamilyRoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Couple_Room model
            return redirect('booking-success')  # Redirect to a success page (you can customize this URL)
    else:
        form = FamilyRoomForm()

    return render(request, 'Family.html', {'form': form})

def book_Group_room(request):
    if request.method == 'POST':
        form = GroupRoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Couple_Room model
            return redirect('booking-success')  # Redirect to a success page (you can customize this URL)
    else:
        form = GroupRoomForm()

    return render(request, 'Group.html', {'form': form})




def book_Six_room(request):
    if request.method == 'POST':
        form = SixBedRoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Couple_Room model
            return redirect('booking-success')  # Redirect to a success page (you can customize this URL)
    else:
        form = SixBedRoomForm()

    return render(request, 'Sixbed.html', {'form': form})

def book_Dormitory(request):
    if request.method == 'POST':
        form = DormitoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Couple_Room model
            return redirect('booking-success')  # Redirect to a success page (you can customize this URL)
    else:
        form = DormitoryForm()

    return render(request, 'Dormitory.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')





