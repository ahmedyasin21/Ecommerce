from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils import timezone
from categories.models import ShopCategory
from shops.models import ShopProfile



# Create your models here.
class ShopRequest(models.Model):

    Gender = (
    ('male','Male'),
    ('female','Female'),
    )

    Approved = (
    ('Approved','Approved'),
    ('Cancel','cancel'),
    )

    requested_user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(("first_name"), max_length=50,null=True)
    last_name = models.CharField(("last_name"), max_length=50,null=True)
    age = models.IntegerField(("age"),null=True)
    gender = models.CharField(("gender"), max_length=50,choices=Gender)
    nationality = models.CharField(("nationality"), max_length=50,null=True)
    country = CountryField()
    state = models.CharField(("state"), max_length=50,null=True)
    city = models.CharField(("city"), max_length=50,null=True)
    zip_code = models.CharField(("zip code"), max_length=50,null=True)
    user_address = models.CharField(("user address"), max_length=50,null=True)
    shop_title = models.CharField(("Shop title"), max_length=50)
    shop_category = models.ForeignKey(ShopCategory, verbose_name=("shop category"), on_delete=models.CASCADE)
    shop_address = models.CharField(("shop address"), max_length=50,null=True)
    request_approve = models.CharField(("request_approval"), max_length=50,choices=Approved,null=True,)
    create_date = models.DateTimeField(("create date"), default=timezone.now)


    
    def __str__(self):
        return self.requested_user.username

    def save(self,*args, **kwargs):
        response = "i'm updated"
        print(response)
        super(ShopRequest,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shoprequests:shop_form_detail", kwargs={"pk": self.pk})
