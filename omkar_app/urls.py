from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
]