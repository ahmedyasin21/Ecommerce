from django.contrib import admin
from .models import ShopRequest
# Register your models here.


class ShopRequestAdmin(admin.ModelAdmin):
    list_display = ['__str__','requested_user']
    class Meta:
        model = ShopRequest

admin.site.register(ShopRequest,ShopRequestAdmin)