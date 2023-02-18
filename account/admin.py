from django.contrib import admin
from .models import Clent
# Register your models here.


class AdminClent(admin.ModelAdmin):
    list_display = ['id','username', 'clent_phone_number', 'kafil', 'kafil_phone_number']
admin.site.register(Clent, AdminClent)

