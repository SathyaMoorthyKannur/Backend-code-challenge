from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','usage_type_id','usage_at','amount']
@admin.register(Usage_types)
class UsagetypeAdmin(admin.ModelAdmin):
    list_display = ['id','name','unit','factor']