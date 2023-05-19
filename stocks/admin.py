from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(StockTransaction)
class AdminUser(admin.ModelAdmin):
    list_display = ["transaction_date","transaction_type","price","quantity"]