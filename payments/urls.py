from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    # path('',cart_home,name ='home'),
    path('stripe/',views.PaymentView.as_view(), name='strip_payment'),

    # path('order-summary/<slug>/',views.OrderDetailView, name='order_summary'),
    # path('checkout',checkout_home,name = 'checkout')
]