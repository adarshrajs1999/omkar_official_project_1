# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('background/', views.background, name='background'),
    path('payment-options/', views.payment_options, name='payment_options'),
    path('cash-payment/', views.cash_payment, name='cash_payment'),
    path('online-payment/', views.online_payment, name='online_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('not_available/',views.not_available,name='not_available'),
    path('book_couple_room/',views.book_couple_room,name='book_couple_room'),
    path('book_Family_room/',views.book_Family_room,name='book_Family_room'),
    path('book_Group_room/',views.book_Group_room,name='book_Group_room'),
    path('book_Six_room/',views.book_Six_room,name='book_Six_room'),
    path('book_Dormitory/',views.book_Dormitory,name='book_Dormitory'),
    path('booking-success/', views.booking_success, name='booking-success'),  # Success page URL
    path('booking/<int:booking_id>/<str:room_type>/details/', views.view_booking_details, name='view-booking-details'),




]

