# booking/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
import razorpay
from .forms import CoupleRoomForm, FamilyRoomForm, GroupRoomForm, DormitoryForm, SixBedRoomForm, CoupleRoomFormAC, \
    FamilyRoomFormAC, GroupRoomFormAC
from .models import Couple_Room, Family_Room, Group_Room, Six_Bed_Room, Dormitory
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from twilio.rest import Client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))



def home(request):
    return render(request,'home.html')


def book_couple_room(request):
    if request.method == 'POST':
        form = CoupleRoomForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data without committing to the database yet

            return redirect('view-booking-details', booking_id=booking.id, room_type='couple')

    else:
        form = CoupleRoomForm()

    return render(request, 'Couple.html', {'form': form})



def book_Family_room(request):
    if request.method == 'POST':
        form = FamilyRoomForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the FamilyRoom model
            return redirect('view-booking-details', booking_id=booking.id, room_type='family')
    else:
        form = FamilyRoomForm()

    return render(request, 'Family.html', {'form': form})


def book_Group_room(request):
    if request.method == 'POST':
        form = GroupRoomForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the GroupRoom model
            return redirect('view-booking-details', booking_id=booking.id, room_type='group')
    else:
        form = GroupRoomForm()

    return render(request, 'Group.html', {'form': form})


def book_Six_room(request):
    if request.method == 'POST':
        form = SixBedRoomForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the SixBedRoom model
            return redirect('view-booking-details', booking_id=booking.id, room_type='sixbed')
    else:
        form = SixBedRoomForm()

    return render(request, 'Sixbed.html', {'form': form})


def book_Dormitory(request):
    if request.method == 'POST':
        form = DormitoryForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the Dormitory model
            return redirect('view-booking-details', booking_id=booking.id, room_type='dormitory')
    else:
        form = DormitoryForm()

    return render(request, 'Dormitory.html', {'form': form})

def CoupleAC_Book(request):
    if request.method == 'POST':
        form = CoupleRoomFormAC(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the Couple_Room model
            return redirect('view-booking-details', booking_id=booking.id, room_type='couple')
    else:
        form = CoupleRoomFormAC()

    return render(request, 'CoupleAC.html', {'form': form})

def FamilyAC_Book(request):
    if request.method == 'POST':
        form = FamilyRoomFormAC(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the Couple_Room model
            return redirect('view-booking-details', booking_id=booking.id, room_type='family')
    else:
        form = FamilyRoomFormAC()

    return render(request, 'FamilyAC.html', {'form': form})

def GroupAC_Book(request):
    if request.method == 'POST':
        form = GroupRoomFormAC(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the Couple_Room model
            return redirect('view-booking-details', booking_id=booking.id, room_type='group')
    else:
        form = GroupRoomFormAC()

    return render(request, 'GroupAC.html', {'form': form})




def view_booking_details(request, booking_id, room_type):
    # Get the booking object based on the room_type and booking_id
    if room_type == 'couple':
        booking = get_object_or_404(Couple_Room, id=booking_id)
        form_class = CoupleRoomForm
        redirect_url = 'book_couple_room'
    elif room_type == 'family':
        booking = get_object_or_404(Family_Room, id=booking_id)
        form_class = FamilyRoomForm
        redirect_url = 'book_Family_room'
    elif room_type == 'group':
        booking = get_object_or_404(Group_Room, id=booking_id)
        form_class = GroupRoomForm
        redirect_url = 'book_Group_room'
    elif room_type == 'sixbed':
        booking = get_object_or_404(Six_Bed_Room, id=booking_id)
        form_class = SixBedRoomForm
        redirect_url = 'book_Six_room'
    elif room_type == 'dormitory':
        booking = get_object_or_404(Dormitory, id=booking_id)
        form_class = DormitoryForm
        redirect_url = 'book_Dormitory'
    else:
        return redirect('not_available')  # In case of an invalid room type

    # Render the form with the booking data
    form = form_class(instance=booking)

    # Make form read-only
    for field in form.fields:
        form.fields[field].widget.attrs['disabled'] = True

    if request.method == 'POST':
        if 'ok' in request.POST:
            return redirect('booking-success',booking_id=booking_id,room_type=room_type)
        elif 'cancel' in request.POST:
            return redirect(redirect_url)

    return render(request, 'view_booking_details.html',{'form': form, 'booking_id': booking_id, 'room_type': room_type})



def booking_success(request, booking_id, room_type):
    global booking
    # Retrieve the booking object based on room type
    if room_type == 'couple':
        booking = get_object_or_404(Couple_Room, id=booking_id)
    elif room_type == 'family':
        booking = get_object_or_404(Family_Room, id=booking_id)
    elif room_type == 'group':
        booking = get_object_or_404(Group_Room, id=booking_id)
    elif room_type == 'sixbed':
        booking = get_object_or_404(Six_Bed_Room, id=booking_id)
    elif room_type == 'dormitory':
        booking = get_object_or_404(Dormitory, id=booking_id)

    # Prepare email content
    subject = f"Booking Confirmation for {room_type.capitalize()} Room"
    message = (f'''
               Details:
               Room Type: {room_type.capitalize()}
               Room Name: {booking.Room_name} 
               Room Amount: {booking.Room_amount}
               Check-in: {booking.Check_in}
               Check-out: {booking.Check_out}
               Name: {booking.Name}
               Phone: {booking.Phone}
               Email: {booking.Email}
               Adults: {booking.Adults}
               Child: {booking.Child}              
               ''')
    recipient_email = 'omkaartouristhome@gmail.com'

    # Send the email
    send_mail(subject, message, 'omkaartouristhome@gmail.com', [recipient_email], fail_silently=False)

    return render(request, 'booking_success.html', {
        'booking': booking,
        'booking_id': booking_id,
        'room_type': room_type
    })


def cash_payment(request, booking_id, room_type):
    # Get the booking object to retrieve name and phone number
    if room_type == 'couple':
        booking = get_object_or_404(Couple_Room, id=booking_id)
    elif room_type == 'family':
        booking = get_object_or_404(Family_Room, id=booking_id)
    elif room_type == 'group':
        booking = get_object_or_404(Group_Room, id=booking_id)
    elif room_type == 'sixbed':
        booking = get_object_or_404(Six_Bed_Room, id=booking_id)
    elif room_type == 'dormitory':
        booking = get_object_or_404(Dormitory, id=booking_id)
    else:
        return redirect('not_available')  # In case of an invalid room type

    # Prepare email content for cash payment
    subject = f"Cash Payment Confirmation for {room_type.capitalize()} Room"
    message = (f'''
               Booking Details:
               Name: {booking.Name}
               Phone: {booking.Phone}
               Room Type: {room_type.capitalize()}
               ''')

    recipient_email = 'omkaartouristhome@gmail.com'  # Your recipient email

    # Send the email
    send_mail(subject, message, 'omkaartouristhome@gmail.com', [recipient_email], fail_silently=False)

    return render(request, 'cash_booking_confirmed.html')




def create_razorpay_order(request, booking_id, room_type):
    room = None  # Initialize the variable to avoid UnboundLocalError

    try:
        # Fetch the appropriate room details based on the room_type
        if room_type == 'couple':
            room = Couple_Room.objects.get(id=booking_id)
        elif room_type == 'family':
            room = Family_Room.objects.get(id=booking_id)
        elif room_type == 'group':
            room = Group_Room.objects.get(id=booking_id)
        elif room_type == 'sixbed':
            room = Six_Bed_Room.objects.get(id=booking_id)
        elif room_type == 'dormitory':
            room = Dormitory.objects.get(id=booking_id)
    except (Couple_Room.DoesNotExist, Family_Room.DoesNotExist, Group_Room.DoesNotExist, Six_Bed_Room.DoesNotExist,
            Dormitory.DoesNotExist):
        return redirect('booking_failure')

    if room:
        # Proceed with Razorpay order creation
        amount = int(room.Room_amount)   # Convert amount to paise
        razorpay_order = razorpay_client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1',
            'notes': {
                'booking_id': booking_id,  # Include booking ID in notes
                'room_type': room_type      # Include room type in notes
            }
        })
        context = {
            'room': room,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key': 'your_razorpay_key',  # Replace with your actual Razorpay key
            'amount': amount,
        }
        return render(request, 'razorpay_payment.html', context)

    return redirect('booking_failure')


@csrf_exempt
def razorpay_payment_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')

        # Verify the payment signature
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            razorpay_client.utility.verify_payment_signature(params_dict)

            # Payment successful
            # Retrieve the Razorpay order to get metadata
            razorpay_order = razorpay_client.order.fetch(order_id)
            booking_id = razorpay_order['notes']['booking_id']  # Extract booking ID
            room_type = razorpay_order['notes']['room_type']     # Extract room type

            # Fetch the booking details based on the booking ID
            if room_type == 'couple':
                booking = get_object_or_404(Couple_Room, id=booking_id)
            elif room_type == 'family':
                booking = get_object_or_404(Family_Room, id=booking_id)
            elif room_type == 'group':
                booking = get_object_or_404(Group_Room, id=booking_id)
            elif room_type == 'sixbed':
                booking = get_object_or_404(Six_Bed_Room, id=booking_id)
            elif room_type == 'dormitory':
                booking = get_object_or_404(Dormitory, id=booking_id)

            # Prepare email content for successful payment
            subject = f"Payment Confirmation for {room_type.capitalize()} Room"
            message = (f'''
                       Booking Details:
                       Name: {booking.Name}
                       Phone: {booking.Phone}
                       Room Type: {room_type.capitalize()}
                       Payment ID: {payment_id}
                       ''')
            recipient_email = 'omkaartouristhome@gmail.com'  # Your recipient email

            # Send the email
            send_mail(subject, message, 'omkaartouristhome@gmail.com', [recipient_email], fail_silently=False)

            # Redirect to the success page
            return redirect('payment_success')

        except razorpay.errors.SignatureVerificationError:
            # Payment failed due to signature mismatch
            return redirect('payment_failure')

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')




