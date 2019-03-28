from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'name', 'funcao', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['username', 'name', 'email']


admin.site.register(User, UserAdmin)

