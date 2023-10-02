from django.contrib import admin

from account.models import UserManager, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'password',]

admin.site.register(User, UserAdmin)

# Register your models here.
