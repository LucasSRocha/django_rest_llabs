from django.contrib import admin

from .models import Product
from .models import WishList
from .models import UserMagalu
# Register your models here.

admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(UserMagalu)
