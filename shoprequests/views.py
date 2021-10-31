from django.shortcuts import render,redirect
from .models import ShopRequest
from .forms import ShopRequestForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.db.models.signals import post_save
from django.dispatch import receiver
from shops.models import ShopProfile
from django.contrib.auth.models import User
# Create your views here.


class ShopRequestCreateView(CreateView):
    model = ShopRequest
    form_class= ShopRequestForm
    template_name = "shoprequests/request_form.html"

    def get(self,request,*args, **kwargs):
        
        try:
            requested_form = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
            requested_form = None
        
        if requested_form is not None:
            print('requested form request_approve',requested_form.request_approve)
            if requested_form.request_approve == 'Approved': #Check if approved 
                print('im inside',requested_form.request_approve)
                try:
                    have_shop = ShopProfile.objects.get(shop_owner=self.request.user) #Check user has a shop
                    print('its got',have_shop)
                except ShopProfile.DoesNotExist:
                    have_shop = None
                    print('its none')
                
                if have_shop is not None: #if he does have a shop then we will sure that
                    sure_shop = ShopProfile.objects.get(shop_owner=self.request.user)
                    print('he has a shop')
                    try:
                        sure_shop = ShopProfile.objects.get(shop_owner=self.request.user)
                        print('his sure shop',sure_shop)
                    except ShopProfile.DoesNotExist:
                        sure_shop = None
                        print('i dont have shop')
                    if sure_shop is not None:
                        print('assigning him a staff person')
                        user = User.objects.get(username=self.request.user.username)
                        user.is_staff = True 
                        user.save()
                        return redirect('shops:shop_profile', slug=sure_shop.slug) 
                else:
                    shop = ShopProfile.objects.create(shop_owner=self.request.user,title=requested_form.shop_title, shop_address=requested_form.shop_address,shop_category=requested_form.shop_category)
                    return redirect('shoprequests:shop_form_detail',pk=requested_form.pk)
            else: #Check if not approved then form detail view
                return redirect('shoprequests:shop_form_detail',pk=requested_form.pk)
            
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

            

    def form_valid(self, form):
        shop_request = form.save(commit=False)
        shop_request.requested_user = self.request.user 
        shop_request.save()
        return super().form_valid(form)



class ShopRequestDetailView(DetailView):
    model = ShopRequest
    context_object_name = 'shop_requests'
    template_name = "shoprequests/form_detail.html"

class ShopRequestUpdateView(UpdateView):
    model = ShopRequest
    form_class= ShopRequestForm
    template_name = "shoprequests/request_form.html"