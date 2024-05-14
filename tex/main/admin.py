from django.contrib import admin
from .models import User, Order, Tovar


admin.site.register(User)
admin.site.register(Tovar)
admin.site.register(Order)