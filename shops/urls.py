from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'shops'

urlpatterns = [
    path('profile/<str:slug>/',views.ShopProfileDetailView.as_view(),name='shop_profile'),
    path('profile/update/<str:slug>/',views.ShopProfileUpdateView.as_view(),name='shop_profile_update')
]
