from django.db import models
from django.contrib import auth
from django.template.defaultfilters import slugify
from source.utils import unique_slug_generator
from django.db.models.signals import pre_save
# To handle with files you can you the following funtions. they will change the path of a file.
import random
from shops.models import ShopProfile
from django.urls import reverse
import os
from django.utils import timezone

def upload_image_path(self, filename):
	return 'product_images/' + str(self.pk) + '/product_image.png'

class Product(models.Model):

    product_owner = models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank =True,unique = True)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2, default = 00.00)
    discount_price = models.DecimalField(max_digits=50, decimal_places=2,blank=True, null=True)
    feature = models.BooleanField(blank=True,null=True)
    create_date = models.DateTimeField(("create date"), default=timezone.now)
    

    #images import
    image_one = models.ImageField( upload_to=upload_image_path,height_field=None, width_field=None, max_length=None,blank = True,null = True)

  
    def __str__(self):
        return self.title

    def get_image_one_filename(self):
        return str(self.image_one)[(self.image_one).index('product_images/' + str(self.pk)+ "/"):]
        
    def get_absolute_url(self,*args, **kwargs):
        return reverse("products:product_detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("products:add_to_cart", kwargs={'slug': self.slug})

    
    def get_remove_from_cart_url(self):
        return reverse("products:remove_from_cart", kwargs={'slug': self.slug})


def product_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever,Product)
    