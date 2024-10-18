# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_couple_room/',views.book_couple_room,name='book_couple_room'),
    path('book_Family_room/',views.book_Family_room,name='book_Family_room'),
    path('book_Group_room/',views.book_Group_room,name='book_Group_room'),
    path('book_Six_room/',views.book_Six_room,name='book_Six_room'),
    path('book_Dormitory/',views.book_Dormitory,name='book_Dormitory'),
    path('booking-success/', views.booking_success, name='booking-success'),  # Success page URL
    path('booking/<int:booking_id>/<str:room_type>/details/', views.view_booking_details, name='view-booking-details'),
    path('booking-success/<int:booking_id>/<str:room_type>/', views.booking_success, name='booking-success'),
    path('cash-payment/<int:booking_id>/<str:room_type>/', views.cash_payment, name='cash_payment'),
    path('create-razorpay-order/<int:booking_id>/<str:room_type>/', views.create_razorpay_order,name='create_razorpay_order'),
    path('razorpay-callback/', views.razorpay_payment_callback, name='razorpay_payment_callback'),
    path('payment_success',views.payment_success,name='payment_success'),
    path('payment_failure',views.payment_failure,name='payment_failure'),


    path('CoupleAC_Book/',views.CoupleAC_Book,name='CoupleAC_Book'),
    path('GroupAC_Book/', views.GroupAC_Book, name='GroupAC_Book'),
    path('FamilyAC_Book/', views.FamilyAC_Book, name='FamilyAC_Book'),

]

