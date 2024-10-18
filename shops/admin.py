# shops/admin.py

from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'created_at')
    search_fields = ('name',)