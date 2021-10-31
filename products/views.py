from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django.views import generic
from carts.models import Cart
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = "products/product_form.html"
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.product_owner = self.request.user.shop_profile
        product.save()
        return super().form_valid(form)


class ProductDetailView(generic.DetailView):
    # login_url = '/accounts/login/'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        # context["cart"] = cart_obj
        return context
    


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    model = Product


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('products:product_list')
        


class ProductListView(generic.ListView):
    
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    # paginate_by = 15
    # def get_queryset(self):
    #     user = get_object_or_404(auth.models.User, username=self.kwargs.get('username'))
    #     return Notes.objects.filter(author=user).order_by('-create_date')




@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    print('got product',product)
    order_product, created = Cart.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    print('ordered product',order_product)
    print('order created',created)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        print('order query set exicts',order_qs.exists())
        order = order_qs[0]
        print('order demanded',order)
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            print('order exists in filter',order)
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
            return redirect("orders:order_summary")
        else:
            order.products.add(order_product)
            print('order not exists in filter',order)
            messages.info(request, "This product was added to your cart.")
            return redirect("products:product_detail",slug=slug)
    else:
        # print('order not exists in start',order)
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
        return redirect("products:product_detail",slug=slug)
    

@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = Cart.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("orders:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("products:product_detail",slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("products:product_detail",slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = Cart.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, "This item quantity was updated.")
            return redirect("orders:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("products:product_detail",slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("products:product_detail",slug=slug)