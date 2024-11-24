from django.contrib import admin

# Register your models here.
# signup/admin.py

from .models import Profile

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'email', 'cast', 'marital_status', 'family_status', 'family_type', 'family_values', 'disability')
    search_fields = ('name', 'email')
    list_filter = ('marital_status', 'family_status', 'family_type', 'family_values', 'disability')
