from django.contrib import admin

# Register your models here.
from .models import Profile
from.models import Cart
from.models import CartItems

admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItems)