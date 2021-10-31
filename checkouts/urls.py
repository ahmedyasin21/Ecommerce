from django.urls import path
from .views import (
    CheckoutView,
    AddCouponView,
)

app_name = 'checkouts'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add_coupon'),
]