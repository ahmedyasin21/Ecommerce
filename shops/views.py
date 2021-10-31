from django.shortcuts import render
from .models import ShopProfile
from .forms import ShopProfileForm
from django.views.generic import CreateView, DetailView, UpdateView
from products.models import Product

# Create your views here.


class ShopProfileDetailView(DetailView):
    model = ShopProfile
    template_name='shops/shop_profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ShopProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['shopprofile']
        context["products_count"] = Product.objects.filter(product_owner=user).count()
        return context
    


class ShopProfileUpdateView(UpdateView):
    model = ShopProfile
    form_class = ShopProfileForm
    template_name = 'shops/shop_profile_update.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ShopProfileUpdateView, self).get_context_data(*args, **kwargs)
        update_form = ShopProfileForm(instance = self.request.user.shop_profile)
        context['form']=update_form
        return context
    
    def form_valid(self, form):
        if self.request == 'POST':
            # shop_title = form.cleaned_data['title']

            form.save()
        return super().form_valid(form)
