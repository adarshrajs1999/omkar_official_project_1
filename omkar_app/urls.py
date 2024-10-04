# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('background/', views.background, name='background'),
    path('check-availability/', views.check_availability, name='check_availability'),
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('payment-options/', views.payment_options, name='payment_options'),
    path('cash-payment/', views.cash_payment, name='cash_payment'),
    path('online-payment/', views.online_payment, name='online_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('not_available/',views.not_available,name='not_available')

]