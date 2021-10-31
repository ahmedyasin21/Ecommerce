from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'shoprequests'

urlpatterns = [
    path('',views.ShopRequestCreateView.as_view(),name='shop_request'),
    path('detail/<int:pk>',views.ShopRequestDetailView.as_view(),name='shop_form_detail'),
    path('update/<str:pk>',views.ShopRequestUpdateView.as_view(),name ='shop_form_update'),
]
