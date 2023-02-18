from django.contrib import admin
from .models import *
# Register your models here.

class CreditAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','imei','description','amount','loan_period','interest_rate','date_created']
admin.site.register(Credit, CreditAdmin)
