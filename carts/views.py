from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.


# def cart_home(request):
#     cart_obj,new_obj = Cart.objects.new_or_get(request)
#     return render(request,'carts/home.html',{'cart':cart_obj})

