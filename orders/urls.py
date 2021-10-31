from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    # path('',cart_home,name ='home'),
    path('order-summary/',views.OrderSummaryView.as_view(), name='order_summary'),
    path('refund/',views.RequestRefundView.as_view(), name='request_refund'),

    # path('order-summary/<slug>/',views.OrderDetailView, name='order_summary'),
    # path('checkout',checkout_home,name = 'checkout')
]