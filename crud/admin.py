from django.contrib import admin
from .models import Client, Purchase, Payment

# Register your models here.
admin.site.register(Client)
admin.site.register(Purchase)
admin.site.register(Payment)