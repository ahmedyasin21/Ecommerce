from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from source.utils import profile_unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
from categories.models import ShopCategory
# Create your models here.



# class ShopProfileManager(models.Manager):



#     def get_queryset(self):
#         return super().get_queryset().filter()






class ShopProfile(models.Model):

    shop_owner = models.OneToOneField(User, related_name='shop_profile', on_delete=models.CASCADE)
    shop_address = models.CharField(_("shop address"), max_length=255)
    title = models.CharField(("shop"), max_length=50)
    slug = models.SlugField(blank =True,unique = True)
    create_date = models.DateTimeField(("create date"), default=timezone.now)
    shop_category = models.ForeignKey(ShopCategory, verbose_name=_("shop category"), on_delete=models.CASCADE)
    shop_bg  =models.ImageField(_("Shop background image"), upload_to="shop_back_grounds",default="shop_default.jpeg" ,height_field=None, width_field=None, max_length=None)
    customers = models.ManyToManyField(User, related_name="customers", verbose_name=_("coutomers"))
    customers_favorite = models.ManyToManyField(User,related_name="customers_favorite", verbose_name=_("customers favorite"))
 
    

    def __str__(self):
        return self.shop_owner.username

    def get_absolute_url(self):
        return reverse("shops:shop_profile_update", kwargs={"slug": self.slug})

def shopprofile_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = profile_unique_slug_generator(instance)
    else:
        instance.slug = profile_unique_slug_generator(instance)
pre_save.connect(shopprofile_pre_save_reciever,ShopProfile)


