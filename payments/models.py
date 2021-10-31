from django.db import models
from django.contrib import auth
# Create your models here.



class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    amount = models.DecimalField( max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
